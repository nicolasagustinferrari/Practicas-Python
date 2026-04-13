texto = "Hola Mundo"
print(texto.upper()) #upper (sirve para poner todo en mayuscula)es un metodo, el metodo es una funcion que viene incluida dentro de un objeto. En este caso "texto"
print(texto.lower())
print(texto.find("Mun"))
print(texto.find("mun"))
nuevoTexto = texto.replace("Mun","Nicolása")
print(texto, nuevoTexto)
print("Mundo" in texto)

a1 = 6
a2 = 18.5

print("El valor de la variable a1 es", a1, "y el valor de la variable a2 es", a2)
print("El valor de la variable a1 es " + str(a1), "y el valor de la variable a2 es " + str (a2))
print("El valor de la variable a1 es %d y el valor de la variable a2 es %.1f" % (a1,a2))
print(f"El valor de la variable a1 es {a1} y el valor de a2 es {a2}")

lista_especial = [1, 2, 3.4, ["a", "b", "c"], True]
print(lista_especial)