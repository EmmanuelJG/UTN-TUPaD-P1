
#Ejercicio 1

#Imprime todos los números enteros desde 0 hasta 100.

for i in range(0, 101):
    print(i)

##################################################################
#Ejercicio 2
#Solicita al usuario un número entero y determina la cantidad de dígitos que contiene.

numero=int(input("Ingrese un numero entero: "))
cantidad_digitos=0

while numero > 0:
     numero=numero//10
     cantidad_digitos +=1

print (f"La cantidad de digitos que tiene es {cantidad_digitos}")

#####################################################################
#Ejercicio 3
#Suma todos los números enteros comprendidos entre dos valores 
# dados por el usuario, excluyendo esos dos valores.

valor1=int(input("Ingrese el primer numero: "))
valor2=int(input("Ingrese el segundo valor: "))


if valor1 == valor2:
    print("Los valores no deben ser iguales.")
else:
    if valor1 < valor2:
        inicio = valor1 + 1
        fin = valor2
    else:
        inicio = valor2 + 1
        fin = valor1

suma=0

for i in range (inicio, fin):
    suma = inicio + suma
    inicio +=1
    
print(f"La suma total de los números entre {valor1} y {valor2} (excluidos) es {suma}")


##############################################################################################
#Ejercicio 4
#Suma los numeros ingresados en secuencia por elusuario. Se detiene al ingresar 0.

numero=int(input("Ingrese un numero entero: "))

suma=0
while (numero != 0):
    suma = numero + suma
    numero=int(input("Ingrese un numero entero: "))
    
print(f"La suma de los numeros ingresados es, {suma}")

################################################################################################
#Ejercicio 5
#Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random

numero_aleatorio = random.randint(0, 9)
numero_intentos = 0
numero = None 


while (numero_aleatorio != numero):
    numero = int(input("Adivina un numero entre 0 y 9: "))
    numero_intentos += 1

print (f"MUY BIEN, el numero a adivinar era {numero_aleatorio}, te tomo {numero_intentos} intentos adivinar.")

###################################################################################################
#Ejercicio 6
#imprime en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1, -1):  
    if i % 2 == 0:
        print(i)

####################################################################################################
#Ejercicio 7
#Calcula la suma de todos los números comprendidos entre 0 y un 
# número entero positivo indicado por el usuario.

numero = int(input("Ingrese un nuemero entero positivo: "))

suma = 0
numero += 1
inicio = 0

if (numero < 0):
    print ("El nuemro ingresado es negativo")
else:
    for i in range (inicio, numero):
        suma = inicio + suma
        inicio += 1

print (f"La suma de todos los numeros de 0 a {numero-1}, es: {suma}")

#########################################################################################
#Ejercicio 8

print ("Tiene que ingresar 100 numeros para identificar cuantos son pares, impares, negativos y positivos")

pares = 0
impares = 0
negativos = 0
positivos = 0
contador = 0

while (contador < 100):
    numero = int(input("Ingrese un numero: "))
    
    if (numero > 0):
        positivos += 1
    else:
        negativos += 1
    
    if (numero %2 == 0):
        pares += 1
    else:
        impares += 1
    
    contador += 1

print(f"""Segun los numero ingresados, estos son los resultados:
PARES: {pares}
IMPARES: {impares}
NEGATIVOS: {negativos}
POSITIVOS: {positivos}""")

###############################################################################
#Ejercicio 9