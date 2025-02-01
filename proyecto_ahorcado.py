import random

import string

print("Juego del ahorcado")

def eleccion_palabra():
    palabras = ["Cocodrilo", "Alexandra", "Matematica", "Progarmacion", 
                "Felicidad", "Harina", "Motor", "Amortiguadores", "Chipa",
                "Celular", "Medias", "Sombrero"]
    return random.choice(palabras)

