#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# 1. Obtener el string del rango (ya sea por argumento o por input)
if len(sys.argv) < 2:
    print("No se informó un rango como argumento (ej. 4-8).")
    entrada = input("Por favor, ingrese el rango (desde-hasta): ")
else:
    entrada = sys.argv[1]

# 2. Procesar el rango "desde-hasta"
try:
    # Dividimos el string por el guion
    partes = entrada.split('-')
    desde = int(partes[0])
    hasta = int(partes[1])

    # 3. Validar y calcular
    if desde > hasta:
        print("Error: El inicio del rango debe ser menor o igual al final.")
    else:
        print(f"Calculando factoriales desde {desde} hasta {hasta}:")
        for i in range(desde, hasta + 1):
            resultado = factorial(i)
            print(f"Factorial {i}! es {resultado}")

except (ValueError, IndexError):
    print("Error: Formato de rango inválido. Use el formato 'N-M' (ej. 4-8).")