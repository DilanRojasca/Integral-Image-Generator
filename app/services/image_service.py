# app/services/image_service.py
import matplotlib.pyplot as plt
import numpy as np

def create_image(equation: str):
    # Interpretar la ecuación y generar los datos para la gráfica
    x = np.linspace(-10, 10, 400)
    y = eval(equation)  # Nota: eval puede ser peligroso, valida el input adecuadamente
    plt.plot(x, y)
    
    # Guardar la imagen en un buffer o archivo
    plt.savefig('app/static/images/generated_image.png')
    
    return 'generated_image.png'
