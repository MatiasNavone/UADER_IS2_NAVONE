#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* Calcula y grafica la Conjetura de Collatz para n=1 a 10000              *
#* Matías Navone (c) IS2 - UADER                                           *
#*-------------------------------------------------------------------------*
import sys
import matplotlib.pyplot as plt

def calcular_iteraciones_collatz(n):
    """Calcula cuántas iteraciones tarda n en llegar a 1 (convergencia)"""
    # Manejo de casos inválidos
    if n <= 0: return 0
    
    iteraciones = 0
    while n != 1:
        # Lógica de Collatz: si n es par -> n/2, si n es impar -> 3n+1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iteraciones += 1
    
    # La secuencia termina cuando n=1. Se repite la secuencia 4-2-1
    return iteraciones

if __name__ == "__main__":
    print("Calculando iteraciones de Collatz para n desde 1 hasta 10000...")
    
    # Listas para guardar los datos del gráfico
    # CONSIGNA: Ordenadas (Y) = n_comienzo, Abscisas (X) = iteraciones
    n_comienzo = []
    iteraciones_convergencia = []
    
    # Límite superior definido en la consigna
    limite = 10000
    
    # Bucle principal para el rango completo
    for n in range(1, limite + 1):
        pasos = calcular_iteraciones_collatz(n)
        
        # Guardamos los datos respetando la consigna
        n_comienzo.append(n) # Irá al eje Y
        iteraciones_convergencia.append(pasos) # Irá al eje X
        
        # Pequeño feedback visual para saber que el programa avanza
        if n % 2000 == 0:
            print(f"Procesando n={n}...")

    # --- Configuración del Gráfico (Matplotlib) ---
    print("\nGenerando el gráfico...")
    plt.figure(figsize=(12, 8)) # Tamaño de la ventana
    
    # Graficamos: plot(X, Y) -> plot(iteraciones, n)
    plt.scatter(iteraciones_convergencia, n_comienzo, s=1, alpha=0.5, color='b')
    
    # Etiquetas respetando el pedido explícito
    plt.title(f"Conjetura de Collatz (n=1 a {limite}) - IS2 Navone")
    plt.xlabel("Abscisas: Número de Iteraciones para Converger") # Eje X
    plt.ylabel("Ordenadas: Número n de Comienzo") # Eje Y
    
    plt.grid(True) # Mostramos la grilla
    print("Mostrando gráfico...")
    plt.show() # ¡Abrir ventana!