"""
La tareílla es a realizar un programa que calcule el promedio de 3 números.
Desarrollo fue mas general ya que funciona para n números no esta limitado solo para 3 numeros. 
"""
# Mensaje de bienvenida.
print ("\n  ******************************************")
print (" *                                        *")
print ("* Bienvenido al calculo de los promedios *")
print (" *                                        *")
print ("  ******************************************\n")

# Recepcion de datos desdel teclado.
numeros_a_promediar = input ("Ingresa los numeros a promediar separados por un espacio y si son numeros reales separados con un '.':\n")

# Usaremos el comando Split para separar la cadena de números.
lista_cadenas_numeros = numeros_a_promediar.split( )

# Creacion y asignacion de valores iniciales.
suma = 0
cantidad_numeros = 0

# Mediante un ciclo para, transformamos datos, calculamos suma de los elementos y calculamos cantidad de los elementos.
for cadena in lista_cadenas_numeros:
    numero = float(cadena)
    suma = suma + numero
    cantidad_numeros = cantidad_numeros + 1

# Calculamos el promedio.
promedio = suma / cantidad_numeros

# Respuesta para el usuario.
print (f"Promedio de los ({cantidad_numeros}) numeros es: ({promedio:.2f}).\n")

# Y al finalizar tenemos un mensaje de agradecimiento para el usuario.
print ("Gracias por confiar en nosotros\n")
