import random

def jugar_adivinanza():
    # Generamos el número secreto entre 1 y 50
    numero_secreto = random.randint(1, 50)
    intentos = 0
    adivinado = False

    print("¡Bienvenido al juego de adivinanza!")
    print("He pensado un número entre 1 y 50. ¿Puedes adivinarlo?")

    while not adivinado:
        # Pedimos el número al usuario
        intento = int(input("Introduce tu número: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta otra vez!")
        elif intento > numero_secreto:
            print("Demasiado alto. ¡Prueba de nuevo!")
        else:
            adivinado = True
            print(f"¡Felicidades! Lo lograste en {intentos} intentos.")

# Ejecutamos el juego
jugar_adivinanza()