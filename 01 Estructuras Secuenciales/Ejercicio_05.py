
#Pide al usuario ingresar una cantidad de segundos 
# y devuelve a cuantas horas equivale

segundos=input("Ingrese la cantidad de segundos: ")
segundos=int(segundos)

hora = segundos / 3600 #calcula las horas que representan los segundos ingresados
hora=int(hora)

minutos= hora * 60 #calcula los minutos que representa la hora calculada
minutos=int(minutos)

#Muestra en pantalla el resultado
print(f"{segundos} segundos equivale a {hora} horas y {minutos} minutos")