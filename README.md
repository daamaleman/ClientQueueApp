# 🗣️ Client Queue Web App con Reconocimiento de Voz y Texto a Voz

Este proyecto es una aplicación web desarrollada con **Flask** que permite gestionar una fila de atención al cliente utilizando **reconocimiento de voz desde el navegador** y síntesis de voz con **gTTS** (Google Text-to-Speech). Es ideal para automatizar el registro y llamado de clientes usando tecnologías accesibles y modernas.

---

## 🚀 Características

- 🎤 Captura del nombre por voz (usando `webkitSpeechRecognition` en el navegador).
- 📝 Visualización en tiempo real de la cola de espera.
- 🔊 Llamado del siguiente cliente mediante voz generada automáticamente con gTTS.
- 💡 Interfaz moderna, limpia y centrada en la experiencia del usuario.
- 🖱️ Navegación fluida entre registro y atención con botones intuitivos.

---

## 📁 Estructura del Proyecto

```
client_queue_project/
├── app.py                # Servidor principal de Flask
├── templates/
│   ├── index.html        # Vista para registrar clientes
│   └── attend.html       # Vista para atender clientes
├── static/
│   ├── script.js         # Lógica de grabación y envío de nombre
│   └── styles.css        # Estilos personalizados
├── requirements.txt      # Dependencias del proyecto
└── README.md             # Documentación del proyecto
```

---

## ⚙️ Requisitos

- Python 3.7 o superior
- Flask
- gTTS (Google Text-to-Speech)

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 🧪 Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/daamaleman/ClientQueueApp.git
cd ClientQueueApp
```

2. Instala los requerimientos:

```bash
pip install -r requirements.txt
```

3. Ejecuta el servidor Flask:

```bash
python app.py
```

4. Abre tu navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 👨‍💻 Autor

**Diedereich Alexander Alemán Martínez**  
Estudiante de Ingeniería en Sistemas de Información - UAM  
📫 Contacto: [diedereicha@uamv.edu.ni](mailto:diedereicha@uamv.edu.ni)

---

## 📝 Licencia

Este proyecto se distribuye bajo la licencia **MIT**. Puedes usarlo, modificarlo y compartirlo libremente.

---

## 🎯 Notas importantes

- El reconocimiento de voz funciona mejor en **Google Chrome**, ya que utiliza `webkitSpeechRecognition`.
- El sistema guarda el audio generado por gTTS en `static/audio.mp3` y lo reproduce automáticamente al llamar al siguiente cliente.
