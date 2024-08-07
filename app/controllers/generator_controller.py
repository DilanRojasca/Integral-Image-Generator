# app/controllers/generator_controller.py
from app.services.image_service import create_image

def generate_image(equation: str):
    # Aquí puedes agregar la lógica para interpretar la ecuación y generar la imagen
    image = create_image(equation)
    return {"image": image}
