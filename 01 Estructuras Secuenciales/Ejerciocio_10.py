
#Pide al usuario ingresar 3 numero y saca el promedio entre los 3

#Pide al usuario ingrresar 3 numeros
num1=input("Ingrese el primer numero:")
num1=float(num1)
num2=input("Ingrese el segundo numero:")
num2=float(num2)
num3=input("Ingrese el tercer numero:")
num3=float(num3)

#Calcula el promedio
promedio= (num1+num2+num3)/3
promedio=float(promedio)

#Imprime en pantalla el resultado del promedio
print(f"El promedio entre los 3 numero ingresados es de {promedio}")