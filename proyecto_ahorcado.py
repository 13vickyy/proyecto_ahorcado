import random

import string

print("Juego del ahorcado")

def eleccion_palabra():
    palabras = ["Cocodrilo", "Alexandra", "Matematica", "Progarmacion", 
                "Felicidad", "Harina", "Motor", "Amortiguadores", "Chipa",
                "Celular", "Medias", "Sombrero"]
    return random.choice(palabras).lower

palabra = eleccion_palabra()

longuitud_guiones = ""

for g in palabra:
    if g:
        longuitud_guiones += "_ "

print("Comencemos...\n RECORDA QUE TENES 6 VIDAS \n La palabra es: ", longuitud_guiones)

eleccion_letra_usr= input=("Ingrese una letra: ")
if eleccion_letra_usr