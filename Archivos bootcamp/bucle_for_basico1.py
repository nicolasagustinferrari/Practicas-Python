
# Ejercicio 1: rango de 0 a 100
for numeros in range(0, 101):
    print(numeros)


# Ejercicio 2: rango de 0 a 500 (incluido) y multiplo de 2
for multiplo in range(0, 501):
    if multiplo % 2 == 0:
        print(multiplo)


# Ejercicio 3: Rango de 0 a 100, multiplo de 5, imprime "ice ice", multiplo de 10, imprime "baby" 
for numero5 in range(0, 101):
    if numero5 % 10 == 0:
        print("baby")
    elif numero5 % 5 == 0:
        print("ice ice")
    else:
        print(numero5)


#Ejercicio 4: Suma los numeros pares del 0 al 500000
suma_total = 0

for suma in range(0, 500001, 2):
    suma_total += suma
print(suma_total)


# Ejercicio 5: Cuenta regresiva en numeros divisibles por 3, desde 2024 hasta antes de llegar a numerosa negativos.
for regresion in range(2024, 0, -3):
    print(regresion)



# Ejercicio 6: Contador dinamico. Declaracion de variables, si el los numeros son multiplos de "Multiplo", los imprmie.
numInicial = 1
numFinal = 20
multiplo = 2

for numero in range(numInicial, numFinal + 1):
    if numero % multiplo == 0:
        print(numero)