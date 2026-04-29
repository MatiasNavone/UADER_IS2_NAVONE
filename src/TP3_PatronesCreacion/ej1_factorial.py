# TP3 - Ejercicio 1: calculo de factorial
# Patron: Singleton

class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("[Singleton] Nueva instancia creada.")
        else:
            print("[Singleton] Reutilizando instancia existente.")
        return cls._instance

    def calcular(self, n: int) -> int:
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado


# --- Demostración ---
if __name__ == "__main__":
    calc1 = FactorialCalculator()
    calc2 = FactorialCalculator()

    print(f"\n¿calc1 y calc2 son la misma instancia? {calc1 is calc2}")

    print(f"\nFactorial de 5  = {calc1.calcular(5)}")
    print(f"Factorial de 10 = {calc2.calcular(10)}")
    print(f"Factorial de 0  = {calc1.calcular(0)}")