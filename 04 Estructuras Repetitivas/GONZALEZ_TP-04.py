
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