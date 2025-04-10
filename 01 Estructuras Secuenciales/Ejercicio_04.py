
#Calcula el area y el perimetro de un circulo.
#El dato del radio lo ingresa el usuario.

radio=input("Ingrese el radio del circulo: ")
radio=float(radio)

area = 3.1415 * radio **2 #Calcula el area
perimetro = 2 * 3.1415 * radio #Calcula el perimetro

#Imprime los resultados del area y el perimetro4
print(f"El area del circulo es {area}, y su perimetro es {perimetro}")
