
#Pasa la temperatura ingresada en celsius a fahrenheit
#Pide al usuario ingresar los grados celsius
temp_celsius=input("Ingrese la temperatura en celsius :")
temp_celsius=int(temp_celsius)

#realiza el calculo para pasar a fahrenheit la temperatura
temp_fahrenheit= 1.8 * temp_celsius + 32

#Muestra en pantalla el resultado de la conversion a fahrenheit
print(f"La temperatura {temp_celsius}° celsius convertida a fahrenheit es de {temp_fahrenheit}°")