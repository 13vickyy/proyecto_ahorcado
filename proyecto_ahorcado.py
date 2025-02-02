import random

import string

print("Juego del ahorcado")

#python elige palabra al azar

def eleccion_palabra():
    palabras = ["Cocodrilo", "Alexandra", "Matematica", "Progarmacion", 
                "Felicidad", "Harina", "Motor", "Amortiguadores", "Chipa",
                "Celular", "Medias", "Sombrero"]
    return random.choice(palabras).lower()

palabra = eleccion_palabra() #eleccion de palabra al azar

#inicio de contadores 

longuitud_guiones = ""
vidas = 6
letras_ingresadas = [] #contador de todas las letras ingresadas por el usr

for g in palabra: #genera cantidad de guiones segun la palabra seleccionada
    if g:
        longuitud_guiones += "_ "

print("Comencemos...\n RECORDA QUE TENES 6 VIDAS \n La palabra es: ", longuitud_guiones)

def mostrar_progreso(palabra,palabra_ingresada):
    resultado=[]
    for letra in palabra:
        if letra in palabra_ingresada: #si la letra la ingreso el usr, se agrega al resultado
            resultado.append(letra)
        else:
            resultado.append("_") #si la letra no fue adivinada, mantiene el guion bajo
    return " ".join(resultado)

while vidas > 0: 
    print(f"\nLetras usadas:{", ".join(letras_ingresadas)}")
    print(f"Vidas restantes: {vidas}")

    print("Progreso: ", mostrar_progreso(palabra, letras_ingresadas)) #muestra progreso

    eleccion_letra_usr = input("Ingrese una letra: ").lower()  #pedir usr letra

    if len(eleccion_letra_usr) != 1 or not eleccion_letra_usr.isalpha(): #primera corroboracion de que el usr ingrese lo pedido, no se descuentan vidas en esta instancia
        print("Recorda: Solo podes ingresar 1 letra a-z\n Ingrese nuevamente una letra valida")
        continue

    if eleccion_letra_usr in letras_ingresadas:
        print(f"Ya usaste la letra {eleccion_letra_usr}. Intenta con una letra valida diferente")
        continue

    letras_ingresadas.append(eleccion_letra_usr) #agrego letra a lista de letras ya ingresadas

    if eleccion_letra_usr in palabra:
        print(f"\nMuy bien! {eleccion_letra_usr} esta en la palabra!")

    else:
        vidas -= 1 #resto 1 vida si el usuario ingresa una letra erronea
        print(f"{eleccion_letra_usr} no esta en la palabra. Perdes una vida")

    if mostrar_progreso(palabra, letras_ingresadas).replace(" ", "") == palabra:
        print(f"\nFelicidades! Adivinaste la palabra: {palabra}")
        break #si el usr advina toda la palabra sale del bucle

    if vidas == 0:
        print(f"\n Se te acabaron todas las vidas, la palabra era {palabra}")
