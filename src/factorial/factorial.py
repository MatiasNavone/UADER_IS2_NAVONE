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
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# --- Modificacion ---

if len(sys.argv) < 2:
    print("No se informó un número como argumento.")
    # Solicitamos el número al usuario de forma interactiva
    entrada = input("Por favor, ingrese el número para calcular su factorial: ")
    num = int(entrada)
else:
    # Si existe el argumento, lo tomamos de la posición 1
    num = int(sys.argv[1])

print("Factorial", num, "! es", factorial(num))