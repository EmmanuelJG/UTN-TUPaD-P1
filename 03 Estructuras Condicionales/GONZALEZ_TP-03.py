
#Ejercicio N°1----------------------------------------------------------------------------------------------
#Pide al usuario ingresar su edad para determinar si es mayor o menor.

edad=input("Ingrese su edad: ") #Ingreso de edad
edad=int(edad)

#Realiza la comparacion de la edad ingresada
if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

#Ejercicio N°2----------------------------------------------------------------------------------------------
#Pide al usuario ingresar su nota para saber si esta aprobado o desaprobado.
#Para estar aprobado su nota debe ser mayor o iguala  6

nota=input("Ingrese su nota: ") #Ingreso de nota
nota=int(nota)

#Realiza la comparacion de la edad ingresada
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprbado")


#Ejercicio N°3---------------------------------------------------------------------------------------------
#Pide al ususario ingresar un numero par, en caso de que no se par, vovlera a pedir un numero.

numero=input("Ingrese un numero: ")
numero=int(numero)

#Se utiliza el modulo para realizar la condicion.
if numero % 2 == 0: 
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#Ejercicio N°4----------------------------------------------------------------------------------------
#Segun la edad ingresada la cataloga en: niño/a, adolecente, adulta/a joven y adulto/a

edad=input("Ingrese su edad: ") #Ingreso de edad
edad=int(edad)

if edad < 12:
    print("Pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print("Pertenece a la categoria Adolecente")
elif edad >= 18 and edad < 30:
    print("Pertenece a la categoria Adulto/a joven")
else:
    print("Pertenece a la categoria Adulto/a")


#Ejercicio N°5---------------------------------------------------------------------------------------------
#Pedir al usuario que ingrese una clave entre 8 y 14 caracteres e informa si es correcta o incorrecta.

contra=input("Ingrese una contraseña entre 8 y 14 caracteres: ")

longitud=len(contra) #cantidad de caracteres de la contraseña

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


#Ejercicio N°6---------------------------------------------------------------------------------------------