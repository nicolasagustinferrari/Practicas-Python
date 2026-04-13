
#multiplicar
def multiplicacion(num1, num2):
    resultado = num1 * num2
    return resultado

resultado_multiplicacion = multiplicacion(10, 5)
print(resultado_multiplicacion)


#promedio
def promedio(num1, num2, num3):
    resultado = num1 + num2 + num3
    resultado = resultado / 3
    return resultado


llamada = promedio(5, 7, 10)
print(llamada)

#promedio resumido
def promedio_notas(num1, num2, num3):
    return (num1 + num2 + num3) / 3

llamada = promedio_notas(2, 2, 5)
print(llamada)


#saludar
def Saludar_usuario(nombre):
    return f"Hola {nombre}, que lindo verte por acá!"

print(Saludar_usuario("Nicolás"))

def calcular_imc (peso, altura):
    imc = peso / altura ** 2
    return f"Tu IMC es, {imc}"

print(calcular_imc(65, 1.80))


def concatenar(a, b):
    return str(b) + str(a)
print(concatenar(7, 15))