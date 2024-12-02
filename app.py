from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import pymysql
from huggingface_hub import InferenceClient
from datetime import datetime
import uvicorn
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import os
from fastapi.staticfiles import StaticFiles



# Cargar las variables desde el archivo .env
load_dotenv()

# Acceder a las variables
huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT", 3306))
database = os.getenv("DB_NAME")

#Key de huggingface
client = InferenceClient(api_key=huggingface_api_key)
app = FastAPI()

# Para hacer estática la imagen
app.mount("/static", StaticFiles(directory="static"), name="static")

# Conexión a MySQL
conn = pymysql.connect(
    host=host,
    user=username,
    password=password,
    port=port,
    cursorclass=pymysql.cursors.DictCursor)


# inicializar la base de datos
def initialize_database():
    try:
        with conn.cursor() as cursor:
            # Crear base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS search_history")
            cursor.execute("USE search_history")
            
            # Crear tabla si no existe
            create_table = '''
            CREATE TABLE IF NOT EXISTS search_history (
                id VARCHAR(255) PRIMARY KEY,
                timestamp DATETIME PRIMARY KEY,
                place TEXT,
                user_request TEXT,
                ai_response TEXT
            )'''
            cursor.execute(create_table)
        conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")




initialize_database()

def save_data(id, timestamp, place: str, user_request: str, ai_response: str):
    try:
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            port=port,
            database="search_history",
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cursor:
            sql = "INSERT INTO search_history (id, timestamp, place, user_request, ai_response) VALUES (%s,%s, %s, %s, %s)"
            cursor.execute(sql, (id, timestamp, place, user_request, ai_response))
        conn.commit()
        conn.close()
        return {"message": "Response saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving response: {e}")
    
def extract_user_prompt(prompt: str) -> str:
    # Encuentra el índice donde comienza "<|user|>" y "<|end|>"
    user_start = prompt.find("<|user|>") + len("<|user|>")
    user_end = prompt.find("<|end|>", user_start)

    # Extraer la parte del prompt perteneciente al usuario
    user_prompt = prompt[user_start:user_end].strip()
    return user_prompt


class ResponseRequest(BaseModel):
    place: str


@app.get("/", response_class=HTMLResponse)
def serve_home():
    try:
        with open("home.html", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Archivo 'home.html' no encontrado.")

    

@app.post("/generate-response/", response_class=JSONResponse)
async def generate_response(request: ResponseRequest):  # Cambiar el argumento a `request`
    place = request.place  # Extraer el lugar desde el JSON
    if not place.strip():
        raise HTTPException(status_code=400, detail="El lugar no puede estar vacío.")

    try:
        # Configuración del modelo con HuggingFaceHub
        llm = HuggingFaceEndpoint(
            endpoint_url="https://api-inference.huggingface.co/models/microsoft/Phi-3.5-mini-instruct",
            huggingfacehub_api_token=huggingface_api_key,
            temperature=0.7,  # Ahora se pasa directamente
            max_length=500    # También se especifica directamente
        )

        # Construcción del template para el prompt
        prompt_template = """
        <|system|>

        Eres un guía turístico experto y apasionado de tu ciudad.

        Tu objetivo es crear un recorrido único y emocionante, lleno de lugares que normalmente no aparecen en los blogs de viajes ni en las guías turísticas convencionales. 
        Conoces cada rincón de tu ciudad y amas compartir sus secretos mejor guardados con los visitantes. Tu pasión es mostrarles el alma auténtica del lugar, desde pequeños negocios 
        familiares hasta rincones llenos de historia olvidada, arte urbano escondido o vistas que solo los locales conocen.

        Cuando respondas, hazlo de manera inspiradora y envolvente, como si estuvieras hablando con un amigo curioso que quiere descubrir la esencia auténtica de tu ciudad. Es importante que:

        Captes la atención: Usa descripciones visuales y detalles que hagan que el oyente "sienta" el lugar antes de visitarlo.
        Conectes emocionalmente: Cuenta historias o anécdotas interesantes sobre los sitios, que resalten su valor histórico, cultural o sentimental.
        Motives la acción: Persuade a tu audiencia para que visiten estos lugares, destacando por qué son experiencias únicas e irrepetibles.
        Piensa que tu público objetivo son personas que valoran experiencias auténticas y diferentes, alejadas de lo típico. ¡Haz que se enamoren de tu ciudad tanto como tú!


        <|end|>

        <|user|>

        Acabo de llegar a {location}, ¿qué puedo visitar aquí?

        <|end|>

        <|assistant|>

        """


        PROMPT = PromptTemplate(template = prompt_template, input_variables = ["location"])
        print(PROMPT)

        #Creamos variable de prompt formateada con el lugar y extraemos a otra variable la parte perteneciente al usuario
        formatted_prompt = PROMPT.format(location=place)
        user_prompt = extract_user_prompt(formatted_prompt)


        # Ejecutar el modelo con el prompt
        response = llm.invoke(formatted_prompt)
        print(user_prompt)
        search_time = datetime.now()
        id = place + "_" + str(search_time)
        # Guarda la respuesta en bbdd
        save_data(id, search_time, place, user_prompt, response)
        # Devuelve la respuesta generada
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@app.get("/search-history/")
async def get_search_history():
    try:
        conn = pymysql.connect(
            host=host,
            user=username,
            password=password,
            port=port,
            database="search_history",
            cursorclass=pymysql.cursors.DictCursor
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM search_history")
            results = cursor.fetchall()
        conn.close()
        return {"search_history": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading search history: {e}")



# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)