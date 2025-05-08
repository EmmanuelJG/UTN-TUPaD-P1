

#Ejercicio 01
#lista con los números del 1 al 100 que sean múltiplos de 4

multiplosde4 = list(range(4, 101, 4))
print(multiplosde4)

#---------------------------------------------------------------
#Ejercicio 02
#Se crea una lista e imprime el penultimo valor

lista = [15, "River", 24, 1000, "La Renga", -18, "Quilmes"]

lista_antepenultimo = lista[4]
lista_antepenultimo_2 = lista[-3] #indexing con num negativo

print(lista_antepenultimo)
print(lista_antepenultimo_2)

#----------------------------------------------------------------
#Ejercicio 03
#lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla

lista_vacia=[]

lista_vacia.append("Dia: 15")
lista_vacia.append("Mes: 08")
lista_vacia.append("Año: 1992")

print(lista_vacia)

#------------------------------------------------------------------
#Ejercicio 04
#Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

#--------------------------------------------------------------------
#Ejercicio 05
# Lo que realiza el codigo es buscar en la lista 'numeros'
# el numero mas alto y eliminarlo.
# Despues imprime la lista pero sin el numero que fue eliminado.

#---------------------------------------------------------------------
#Ejercicio 06
#Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

numeros = list(range(10,31,5))

print(numeros[:2])
print(numeros[0], numeros[1])

#----------------------------------------------------------------------
#Ejercicio 07
#Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
# cualesquiera.

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "bora"
autos[2] = "vento"

print(autos)

#------------------------------------------------------------------------
#Ejercicio 08
#Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

dobles = []

dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)

print(dobles)

#---------------------------------------------------------------------------
#Ejercicio 09
#lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo") #a)
compras[1].remove("fideos") #b)
compras[1].append("tallarines") #b)
compras[0].remove("pan") #c)

print(compras) #d)

#-----------------------------------------------------------------------------
#Ejercicio 10
#Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)