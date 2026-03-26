#!/usr/bin/python
import sys

def factorial(num): 
    if num < 0: return 0
    elif num == 0: return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# 1. Obtener la entrada
if len(sys.argv) < 2:
    print("No se informó un rango (ej. -10 o 50-).")
    entrada = input("Por favor, ingrese el rango: ")
else:
    entrada = sys.argv[1]

# 2. Procesar el rango con límites dinámicos
try:
    partes = entrada.split('-')
    
    # Caso "-hasta" (ej. -10) -> desde 1 hasta N
    if partes[0] == "" and partes[1] != "":
        desde = 1
        hasta = int(partes[1])
    
    # Caso "desde-" (ej. 50-) -> desde N hasta 60
    elif partes[0] != "" and partes[1] == "":
        desde = int(partes[0])
        hasta = 60
    
    # Caso "desde-hasta" (ej. 4-8)
    else:
        desde = int(partes[0])
        hasta = int(partes[1])

    # 3. Validación y Bucle de cálculo
    if desde > hasta:
        print("Error: El inicio del rango es mayor al final.")
    else:
        print(f"Calculando desde {desde} hasta {hasta}:")
        for i in range(desde, hasta + 1):
            print(f"Factorial {i}! es {factorial(i)}")

except (ValueError, IndexError):
    print("Error: Formato inválido. Use 'N-M', '-M' o 'N-'.")