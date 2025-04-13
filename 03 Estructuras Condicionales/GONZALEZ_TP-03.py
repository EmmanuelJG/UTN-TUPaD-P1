
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
#Caraga una lista de numeros aleatorios y segun su media, mediana y medio,
#calcula si pertenece a sesgo positivo, negativo o sin sesgo

from statistics import mode, median, mean 
#se importa las funciones mode, median, mean desde libreria statistics

import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria

moda= mode(numeros_aleatorios)
mediana= median(numeros_aleatorios)
media= mean(numeros_aleatorios)

#Condicion que indica que sesgo hay
if media > mediana and mediana > moda:
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda:
    print ("Hay sesgo negativo")
elif media == mediana and mediana == moda and moda == media:
    print ("Sin sesgo")
else:
    pass

#Ejercicio N°7---------------------------------------------------------------------------------------------
#Pide alusuario ingresar una frase o palabra, e indica si termina en vocal

palabra=input("Ingrese una palabra o frase, si termina en vocal se le agregara un signo de exclamacion, de lo contrario quedara igual: ")

if palabra[-1].lower() in "aeiou":
    print (palabra +"!")
else:
    print (palabra)

#Ejercicio N°8---------------------------------------------------------------------------------------------
#Le pide al ususario ingresar su nombre y elelgir si quiere que este todo en
#mayuscula, minuscula o solo la priumer letra.

nombre=input("Ingrese su nombre: ")
opcion=input("""
Seleccione por numero, como quiere visualizar su nombre:
1-Todo en mayuscula
2-Todo en minuscula
3-Mayuscula solo en la primera letra
Elegir opcion: """)

opcion=int(opcion)

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title()) 
else:
    print("ERROR, tiene que elegir entre las opciones 1, 2 y 3.")

#Ejercicio N°9---------------------------------------------------------------------------------------------
#El usuario debe ingresar numero segun la escala de Richter para clasificar la magnitud de un terremoto.

num_escala=input("Ingrese un numero en la escala de Richter: ")
float=float(num_escala)

num_escala = float(input("Ingrese un número en la escala de Richter: "))

if num_escala < 3.0:
    print("Terremoto Muy Leve, imperceptible")
elif num_escala < 4.0:
    print("Terremoto Leve, ligeramente perceptible")
elif num_escala < 5.0:
    print("Terremoto Moderado, sentido por personas, pero generalmente no causa daños.")
elif num_escala < 6.0:
    print("Terremoto Fuerte, puede causar daños en estructuras débiles.")
elif num_escala < 7.0:
    print("Terremoto Muy Fuerte, puede causar daños significativos.")
else:
    print("Terremoto Extremo, puede causar graves daños a gran escala.")

#Ejercicio N°10---------------------------------------------------------------------------------------------
#A partir de el dia, mes y emisferio que ingrese el usuario, se devolvera en que estacion del clima esta.

emisferio=input("Ingrese en que emisferio esta, utilice S si es SUR, o N si es NORTE: ").upper()
dia=int(input("Ingrese el dia: "))
mes=int(input("Ingrese el mes, en numero: "))


if emisferio == "S":
   if (dia >= 21 and mes == 3) or (mes == 4 or mes == 5) or (dia <= 20 and mes == 6):
    print("Estacion Otoño")
   elif (dia >= 21 and mes == 6) or (mes == 7 or mes == 8) or (dia <= 20 and mes == 9):
    print ("Estacion Invierno")
   elif (dia >= 21 and mes == 9) or (mes == 10 or mes == 11) or (dia <= 20 and mes == 12):
    print ("Estacion Primavera")
   else:
    print("Estacion Verano")

elif emisferio == "N":
   if (dia >= 21 and mes == 3) or (mes == 4 or mes == 5) or (dia <= 20 and mes == 6):
    print("Estacion Primavera")
   elif (dia >= 21 and mes == 6) or (mes == 7 or mes == 8) or (dia <= 20 and mes == 9):
    print ("Estacion Verano")
   elif (dia >= 21 and mes == 9) or (mes == 10 or mes == 11) or (dia <= 20 and mes == 12):
    print ("Estacion Otoño")
   else:
    print("Estacion Invierno")
else:
   print("Emisferio no valido")
