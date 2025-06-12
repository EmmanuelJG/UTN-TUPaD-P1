
#Ejercicio 1/////////////////////////////////////////////////////////
# Función para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    

# Programa principal
numero = int(input("Ingresa un número entero positivo: "))

print(f"\nFactoriales del 1 al {numero}:")
for i in range(1, numero + 1):
    print(f"{factorial(i)5}")

#Ejercicio 2////////////////////////////////////////////////////////////////
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Programa
posicion = int(input("Ingresa la posición hasta donde deseas mostrar la serie de Fibonacci: "))

print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
for i in range(posicion + 1):
    print(f"F({i}) = {fibonacci(i)}")

#Ejercicio 3////////////////////////////////////////////////////////////////////////////////////////
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")