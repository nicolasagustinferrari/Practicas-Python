# ==========================================
# GUÍA RÁPIDA DE PYTHON PARA ANÁLISIS DE DATOS
# ==========================================

# 1. TIPOS DE DATOS (Los Átomos)
# Sirven para definir qué estamos procesando.

nombre_producto = "Teclado Mecánico"  # String (Texto) - Siempre entre comillas
precio = 55.50                        # Float (Decimal)
cantidad = 10                         # Int (Entero)
es_valido = True                      # Bool (Booleano) - True o False

# 2. ESTRUCTURAS DE DATOS (Los Archivadores)
# Sirven para agrupar información.

# LISTAS: Ordenadas y modificables. Ideales para columnas de datos.
ventas_semanales = [150, 200, 180, 220] 
ventas_semanales.append(250) # Agrega un valor al final

# DICCIONARIOS: Clave-Valor. Como una fila de una tabla de Excel.
usuario = {
    "id": 1,
    "nombre": "Patricio",
    "puesto": "Analista"
}

# TUPLAS: No se pueden cambiar. Para datos que deben ser fijos.
dimensiones_pantalla = (1920, 1080)

# 3. CONDICIONALES (La Lógica)
# Para que el programa tome decisiones.

stock = 5
if stock == 0:
    print("Sin inventario")
elif stock < 10:
    print("Inventario bajo - Hacer pedido")
else:
    print("Stock suficiente")

# 4. BUCLES / LOOPS (La Automatización)
# Para repetir tareas sobre muchos datos.

# FOR: Recorre cada elemento de una lista.
print("Listado de Ventas:")
for venta in ventas_semanales:
    print(f"Venta del día: ${venta}")

# WHILE: Repite mientras se cumpla una condición.
contador = 5
while contador > 0:
    print(f"Iniciando en... {contador}")
    contador -= 1

# 5. FUNCIONES (Tus Herramientas)
# Bloques de código que reutilizas para no escribir lo mismo mil veces.

def calcular_total(precio_unitario, cantidad_items):
    total = precio_unitario * cantidad_items
    return total

# Llamada a la función
pago_final = calcular_total(precio, cantidad)
print(f"El total a pagar es: {pago_final}")

# 6. LIBRERÍAS (El Siguiente Nivel)
# En análisis de datos, importarás "superpoderes" externos:
# import pandas as pd -> Para tablas y excels.
# import numpy as np  -> Para cálculos matemáticos.




Gastos_Mensuales = [150, 550, 80, 400, 720]
Total = 0
for gasto in Gastos_Mensuales:
    Total = Total + gasto

    if gasto > 500:
        print(f"¡Alerta! Gasto elevado detectado: {gasto}") 

print(f"El gasto total del mes es: {Total}")

#Tipos de datos
#Enteros = int
Precio = 20
#Flotantes = float
Precio = 49,1
#Booleanos = True o False
mayor_edad = True
tiene_tatuajes = False
#Cadenas de texto 
frase = "Hoy es Lunes"


#Tipos de datos compuestos
#Listas [] LOS DATOS PUEDEN CAMBIARSE 
lista_vacia = []
mascotas = ["Lali", "Nala", "Roger", "Luna", "Putuno"]
print(mascotas[1]) #Imprimte/muestra : "Nala"
mascotas[1] = "Tom" #Reemplaza en la posicion 1 de la lista "Nala" por "Lali"
#Para agregar a la lista 
mascotas.append("Goofy")
#Para sacara de la lista 
mascotas.pop(1) #Elimina en este caso, a "Nala"


#Tuplas = Datos que no se pueden modificar y contiene un conjunto de distintos valores
perro = ("Roger", "San Bernardo", "Bariloche", 9)


#Diccionarios = Permite almacenar conenitod a través de una llave y valor, se puede acceder a sus datos de su índice único (Se le llama llave o clave)
diccionario_vacio = {}
persona = {"Nombre": "Nicolás", "Edad": 23, "Altura": 1.80, "usa_lentes": True}
persona ["Nombre"] = "Agustín" #Actualiza el valor si la llave existe 
persona ["Estudios"] = "Analisis de datos" #Agrega esa clave - valaor si no existe previamente.

print(persona) #imprime: {"Nombre": "Agustín", "Edad": 23, "Altura": 1.80, "usa_lentes": True, "Estudios": "Analisis de datos"}

altura = persona.pop("Altura") #elimina la clave indicada y devuelve el valor
print(altura) #imprime: 1.80
print(persona) #imprime: {"Nombre": "Agustín", "Edad": 23, "usa_lentes": True, "Estudios": "Analisis de datos"}


#Funciones comúnes
print(type(3.1416)) #Imprime: <class 'float'>
print(type(persona)) #Imprime: <class 'dict'>

#Para saber el tamaño de una cadena, lista, diccionario, tuplas, utilizamos "len" de length
print(len(persona)) #Imprime 12 (la cantidad de caracteres)
print(len("Me encanta programar")) #Imprime: 20