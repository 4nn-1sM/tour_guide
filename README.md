![imagen_guia](images/readme_image.png)
"""
# 🌍 **Descubre Rincones que Cuentan Historias**  
**Transforma tus viajes con experiencias únicas y relatos envolventes.**

## 🛠️ **Descripción del Proyecto**  
Bienvenido a **Descubre Rincones que Cuentan Historias**, una aplicación diseñada para invitarte a explorar ciudades desde una perspectiva única. Con la ayuda de inteligencia artificial, esta app no solo te sugiere lugares a visitar, sino que los envuelve en relatos inspiradores que capturan el alma de cada rincón. 

Imagina caminar por una plaza histórica, sentir el aroma de una cocina tradicional mezclada con lo moderno, o descubrir arte escondido en calles empedradas... Nuestra misión es que vivas cada destino como si lo experimentaras a través de los ojos de un apasionado narrador local.

Desde pequeños cafés llenos de historias hasta parques donde la naturaleza y el arte convergen, esta aplicación te ayudará a conectar emocionalmente con los lugares que visitas.

---

## ✨ **Características**
- **Relatos inmersivos:** Recibe recomendaciones detalladas y narradas de manera inspiradora sobre los lugares más emblemáticos y escondidos.
- **Historial de búsquedas:** Accede fácilmente a tus exploraciones pasadas para revivir los recuerdos.
- **Interfaz intuitiva:** Un diseño fácil y accesible que realza tu experiencia.
- **IA narrativa personalizada:** Potenciado por el modelo de Hugging Face \`microsoft/Phi-3.5-mini-instruct\` para generar textos que combinan historia, cultura y emoción.
- **Exploración cultural:** Descubre rincones auténticos que reflejan la esencia única de cada ciudad.

---

## 🚀 **Cómo Empezar**

### 1️⃣ **Clona el repositorio**
\`\`\`bash
git clone https://github.com/tuusuario/descubre-rincones.git
cd descubre-rincones
\`\`\`

### 2️⃣ **Configura el entorno**
Crea un archivo \`.env\` en la raíz del proyecto con las siguientes variables:
\`\`\`env
HUGGINGFACE_API_KEY=tu_clave_de_huggingface
DB_USERNAME=tu_usuario_mysql
DB_PASSWORD=tu_contraseña_mysql
DB_HOST=localhost
DB_PORT=3306
\`\`\`

### 3️⃣ **Instala las dependencias**
Asegúrate de tener Python 3.9+ y ejecuta:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4️⃣ **Inicia la aplicación**
\`\`\`bash
uvicorn app:app --reload
\`\`\`
Accede a la app en tu navegador en [http://localhost:8000](http://localhost:8000).

---

## 🖼️ **Vista Previa**

### **Ejemplo de Respuesta**
**Madrid**  
_Bienvenido a Madrid, la vibrante capital de España, donde cada calle, plaza y esquina tiene su propia historia para contar..._


## 🧪 **Pruebas**
Este proyecto incluye una suite de tests básicos para asegurar su funcionalidad.  

### **Ejecutar Tests**
\`\`\`bash
pytest test_app.py
\`\`\`

--- 

¡Espero que disfrutes explorando rincones únicos tanto como yo disfruté creando esta aplicación! 🌟
"""
