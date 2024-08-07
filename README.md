# Graphical Integral Solver

Este proyecto es una aplicación web que permite ingresar integrales y generar gráficas interactivas en 3D. La aplicación está construida utilizando FastAPI en el backend y una combinación de HTML, CSS y JavaScript (con Three.js y Plotly.js) en el frontend. El proyecto sigue el patrón de diseño MVC (Modelo-Vista-Controlador) para una mejor organización y mantenibilidad del código.

## Estructura del Proyecto

project_root/
├── backend/
│ ├── app/
│ │ ├── init.py
│ │ ├── models.py
│ │ ├── views.py
│ │ ├── controllers.py
│ ├── main.py
│ └── requirements.txt
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
└── README.md

bash
Copiar código

## Requisitos Previos

Asegúrate de tener instalados los siguientes programas en tu sistema:

- Python 3.8+
- Node.js (opcional, pero recomendado para manejar dependencias de JavaScript)
- pip (administrador de paquetes de Python)

## Configuración del Proyecto

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:
```bash
git clone <URL_DEL_REPOSITORIO>
cd project_root
2. Configuración del Backend
Navega al directorio del backend:

bash
Copiar código
cd backend
Crea un entorno virtual y actívalo:

bash
Copiar código
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
Instala las dependencias:

bash
Copiar código
pip install -r requirements.txt
Ejecuta el servidor FastAPI:

bash
Copiar código
uvicorn main:app --reload
El servidor se ejecutará en http://localhost:8000.

3. Configuración del Frontend
Abre el archivo frontend/index.html en tu navegador favorito.
La aplicación cargará una interfaz donde podrás ingresar una expresión matemática, una variable, y los límites inferior y superior para la integración.
La gráfica de la integral ingresada se mostrará en un gráfico 3D interactivo.
Uso de la Aplicación
Abre el archivo frontend/index.html en tu navegador.
La aplicación cargará una interfaz donde podrás ingresar una expresión matemática, una variable, y los límites inferior y superior para la integración.
La gráfica de la integral ingresada se mostrará en un gráfico 3D interactivo.
Estructura del Código

Backend

app/init.py: Inicializa el paquete y configura la aplicación FastAPI.

app/models.py: Define los modelos de datos utilizando Pydantic.

app/views.py: Define las rutas y las vistas para la aplicación.


app/controllers.py: Contiene la lógica de negocio para la integración de funciones.
Frontend
index.html: Estructura principal del frontend.

style.css: Estilos para la interfaz de usuario.

script.js: Lógica interactiva para las gráficas y la comunicación con el backend.


Contribuciones Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.

Licencia
Este proyecto está licenciado bajo la MIT License.