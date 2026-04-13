
# Multiplica por 2:
print("====== multiplica por 2 ======")
""""
def multiplica_por_dos(num): # Defino la función y le agrego el limite (parametro)
    resul_lista = []         # Creamos la lista vacía
    for i in range(num + 1): # Definimos el bucle
        valor_multiplicado = (i * 2)
        resul_lista.append(valor_multiplicado)

    return resul_lista   # Return para finalizar la funcion y que el print funcione


print(multiplica_por_dos(5))
"""

# Suma y resta:
print("====== Suma y resta ======")
"""
def suma_y_resta(lista):
    suma = lista[0] + lista[1]
    print(suma)
    resta = lista[0] - lista[1]
    return resta
print(suma_y_resta([5,4]))

"""

# Sumatoria menos longitud
print("====== Sumatoria menos longitud ======")
""""
def sumatoria_menos_longitud(lista):
    suma_total = sum(lista)
    longitud = len(lista)
    resultado = suma_total - longitud
    return resultado
print(sumatoria_menos_longitud([1, 2, 3, 4]))

"""

# Valores multiplicados por el segundo
print("====== Sumatoria menos longitud ======")
""""
def valores_multiplicados_segundo(lista):
    if len(lista) < 2: 
        return []
    multiplicador = lista[1] # Guardo el segundo número para usarlo de multiplicador
    nueva_lista = []         # Genero una nueva lista
    for numero in lista:
        resultado = numero * multiplicador # Genero una variable para guardar numero * multiplicador
        nueva_lista.append(resultado)      # Invoco la variable anteriormente escrita, "nueva_lista" y le agrego un .append(resultado) para guardar las multiplicaciones y generar esa nueva lista
    return nueva_lista

print(valores_multiplicados_segundo([2, 5, 6, 7]))

"""
# Valores multiplicados por el segundo
print("====== Valor multiplicado y longitud ======")

def valor_multiplicado_longitud(valor, longitud):
    longitudNueva = valor * longitud # Calculo el "número mágico" que va a ir en todas las posiciones
    nueva_lista = []                 # Genero una nueva lista vacía
    for i in range(longitud):        # El bucle que se repite la cantidad de veces que diga 'longitud'
        nueva_lista.append(longitudNueva) # Agrego el numero de "longitudnueva" a la nueva lista.
    return nueva_lista

print("Bienvenido al multiplicador")
usuario_valor = int(input("Ingrese el número multiplicador: "))
usuario_longitud = int(input("Ingrese que tamaño tendrá la lista: "))

resultado_final = valor_multiplicado_longitud(usuario_valor, usuario_longitud)
print(f"Tu lista generada es: {resultado_final}")