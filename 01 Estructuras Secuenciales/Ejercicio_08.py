
#Calcula indice de masa corporal al ingresar la altura y su peso

#Pide ingresar los datos de peso y altura
altura=input("Ingrese su altura en Mtr: ")
altura=float(altura)

peso=input("Ingrese su peso en Kg: ")
peso=float(peso)

#Calcula el indice de masa corporal
imc= peso / (altura**2)

#Muestra en pantalla el resultado
print(f"Su indice de masa corporal es de: {imc}")