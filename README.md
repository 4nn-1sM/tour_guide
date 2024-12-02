![imagen_guia](images/readme_image.png)
# 🌍 **Descubre Rincones que Cuentan Historias**  
**Una app para explorar lugares únicos y experiencias inolvidables.**

## 🛠️ **Descripción del Proyecto**  
Esta aplicación web está diseñada para ayudarte a descubrir los secretos mejor guardados de cualquier ciudad. Usando inteligencia artificial, proporciona recomendaciones auténticas e inspiradoras sobre lugares que no suelen aparecer en las guías turísticas tradicionales. Desde pequeñas tiendas familiares hasta arte urbano oculto, ¡esta app te hará sentir como un local en cualquier ciudad que visites!  

---

## ✨ **Características**
- **Recomendaciones únicas:** Explora rincones ocultos y experiencias auténticas.
- **Historial de búsqueda:** Consulta tus búsquedas pasadas y mantén un registro de tus descubrimientos.
- **Interfaz intuitiva:** Diseño moderno y funcional inspirado en **Tailwind CSS**.
- **IA personalizada:** Potenciado por el modelo de Hugging Face \`microsoft/Phi-3.5-mini-instruct\`.
- **Base de datos MySQL:** Guarda y gestiona el historial de búsquedas.

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
Accede a la app en tu navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## 🖼️ **Vista Previa**

### **Pantalla Principal**
![Pantalla Principal](https://via.placeholder.com/800x400.png?text=Captura+de+Pantalla+1)

### **Resultados de Búsqueda**
![Resultados](https://via.placeholder.com/800x400.png?text=Captura+de+Pantalla+2)

---

## 📂 **Estructura del Proyecto**

\`\`\`plaintext
📦 descubre-rincones
├── app.py               # Lógica principal de la aplicación.
├── home.html            # Plantilla HTML con diseño responsivo.
├── static/              # Archivos estáticos (imágenes, CSS).
├── .env                 # Configuración de variables de entorno.
├── requirements.txt     # Dependencias del proyecto.
└── README.md            # Documentación del proyecto.
\`\`\`

---

## 🧪 **Pruebas**
Este proyecto incluye una suite de tests básicos para asegurar su funcionalidad.  

### **Ejecutar Tests**
\`\`\`bash
pytest test_app.py
\`\`\`

---

## 🤝 **Contribuciones**
¡Las contribuciones son bienvenidas! Por favor, sigue estos pasos:  
1. Haz un fork del repositorio.  
2. Crea una nueva rama: \`git checkout -b feature/nueva-caracteristica\`.  
3. Haz tus cambios y realiza un commit: \`git commit -m "Añadida nueva característica"\`.  
4. Envía tus cambios: \`git push origin feature/nueva-caracteristica\`.  
5. Abre un Pull Request en GitHub.  

---

## 📄 **Licencia**
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más información.

---

## ✨ **Agradecimientos**
- **Hugging Face** por su potente API de modelos de lenguaje.
- **Tailwind CSS** por facilitar un diseño moderno y atractivo.
- A ti, por apoyar este proyecto. ❤️

---

## 📫 **Contacto**
Si tienes preguntas o sugerencias, no dudes en escribirme:  
📧 **[tu-email@example.com](mailto:tu-email@example.com)**  
🐦 **[Twitter](https://twitter.com/tuusuario)**  
🌐 **[Sitio web personal](https://tusitio.com)**

--- 

¡Espero que disfrutes explorando rincones únicos tanto como yo disfruté creando esta aplicación! 🌟
"""

# Guardar en un archivo README.md
with open("README.md", "w", encoding="utf-8") as archivo:
    archivo.write(contenido_readme)

print("README.md generado correctamente.")
