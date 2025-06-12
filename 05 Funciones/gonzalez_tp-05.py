
#Ejercicio 01////////////////////////////////////////////////////////////////////
# Definicion de la funcion
def hola_mundo():
    print("Hola Mundo!")

# Llamado a la funcion
if __name__ == "__main__":
    hola_mundo()


#Ejercicio 02/////////////////////////////////////////////////////////////////////////
# Definición de la función
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
if __name__ == "__main__":
    nombre_usuario = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)

#Ejercicio 03//////////////////////////////////////////////////////////////////////////
# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("¿Dónde vives?: ")

    informacion_personal(nombre, apellido, edad, residencia)

#Ejercicio 04/////////////////////////////////////////////////////////////////////////////
# Función calcular el area del circulo
def calcular_area_circulo(radio):
    pi = 3.1416
    return pi * radio ** 2

# Función calcular el perimetro del circulo
def calcular_perimetro_circulo(radio):
    pi = 3.1416
    return 2 * pi * radio

# Programa principal
if __name__ == "__main__":
    radio = float(input("Ingresa el radio del circulo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)

    print(f"El área del circulo es: {area}")
    print(f"El perímetro del circulo es: {perimetro}")

#Ejercicio 05///////////////////////////////////////////////////////////////////////////////
# Función para convertir segundos a horas, 1hora=3600 segundos
def segundos_a_horas(segundos):
    return segundos / 3600  

# Programa principal
if __name__ == "__main__":
    segundos = float(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")