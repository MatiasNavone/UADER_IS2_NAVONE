#!/usr/bin/python
import sys

class Factorial:
    def __init__(self):
        # El constructor puede estar vacío o inicializar algo si fuera necesario
        pass

    def _calcular_individual(self, num):
        """Método interno para el cálculo de un solo factorial"""
        if num < 0: return 0
        elif num == 0: return 1
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

    def run(self, min_val, max_val):
        """Método solicitado para calcular el rango"""
        print(f"--- Ejecutando desde Clase Factorial (Rango: {min_val}-{max_val}) ---")
        for i in range(min_val, max_val + 1):
            resultado = self._calcular_individual(i)
            print(f"Factorial {i}! es {resultado}")

# --- Lógica de Interfaz (fuera de la clase) ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        entrada = input("Ingrese el rango (ej. 4-8): ")
    else:
        entrada = sys.argv[1]

    try:
        partes = entrada.split('-')
        # Reutilizamos la lógica de límites que ya tenías
        desde = int(partes[0]) if partes[0] != "" else 1
        hasta = int(partes[1]) if partes[1] != "" else 60
        
        # INSTANCIAMOS LA CLASE Y CORREMOS EL MÉTODO
        obj_factorial = Factorial()
        obj_factorial.run(desde, hasta)

    except (ValueError, IndexError):
        print("Error en el formato del rango.")