"""
TP - Patrones de Comportamiento
Punto 1: Chain of Responsibility
Cadena de responsabilidad para procesar números del 1 al 100.
- PrimosHandler: consume números primos
- ParesHandler:  consume números pares
- Si ninguno lo consume, se marca como "no consumido"
"""

from abc import ABC, abstractmethod


# ─────────────────────────────────────────────
# Interfaz base del Handler
# ─────────────────────────────────────────────
class Handler(ABC):
    """Interfaz abstracta que define el contrato de la cadena."""

    def __init__(self):
        self._next: Handler | None = None

    def set_next(self, handler: "Handler") -> "Handler":
        """Encadena el siguiente handler y lo devuelve para poder encadenar en línea."""
        self._next = handler
        return handler

    def handle(self, numero: int) -> bool:
        """
        Intenta procesar el número.
        Si no puede (o decide pasar) delega al siguiente en la cadena.
        Retorna True si algún handler lo consumió, False si ninguno lo hizo.
        """
        if self._next:
            return self._next.handle(numero)
        return False          # nadie lo consumió


# ─────────────────────────────────────────────
# Handlers concretos
# ─────────────────────────────────────────────
class PrimosHandler(Handler):
    """Consume el número si es primo."""

    @staticmethod
    def _es_primo(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def handle(self, numero: int) -> bool:
        if self._es_primo(numero):
            print(f"  [PrimosHandler]  {numero:3d} → PRIMO     ✔ consumido")
            return True          # lo consume; NO pasa al siguiente
        # No lo puede consumir; pasa al siguiente
        return super().handle(numero)


class ParesHandler(Handler):
    """Consume el número si es par (y no primo, ya que primos van primero)."""

    def handle(self, numero: int) -> bool:
        if numero % 2 == 0:
            print(f"  [ParesHandler]   {numero:3d} → PAR       ✔ consumido")
            return True
        return super().handle(numero)


# ─────────────────────────────────────────────
# Programa principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Chain of Responsibility — números del 1 al 100")
    print("=" * 55)

    # Construcción de la cadena: Primos → Pares → (fin)
    h_primos = PrimosHandler()
    h_pares  = ParesHandler()
    h_primos.set_next(h_pares)

    no_consumidos = []

    for n in range(1, 101):
        consumido = h_primos.handle(n)
        if not consumido:
            no_consumidos.append(n)

    print()
    print("-" * 55)
    print(f"Números NO consumidos por ningún handler ({len(no_consumidos)}):")
    print(" ", no_consumidos)
    print("=" * 55)