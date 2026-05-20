"""
TP - Patrones de Comportamiento
Punto 2: Iterator
Clase que almacena una cadena de caracteres y expone dos iteradores:
  - DirectoIterator:  recorre de izquierda a derecha
  - ReversoIterator:  recorre de derecha a izquierda
"""

from __future__ import annotations
from abc import ABC, abstractmethod


# ─────────────────────────────────────────────
# Interfaz Iterator
# ─────────────────────────────────────────────
class StringIterator(ABC):
    """Define la interfaz común para todos los iteradores de cadena."""

    @abstractmethod
    def has_next(self) -> bool:
        """¿Quedan elementos por recorrer?"""
        ...

    @abstractmethod
    def next(self) -> str:
        """Devuelve el próximo carácter y avanza el cursor."""
        ...

    def __iter__(self):
        return self

    def __next__(self):
        if not self.has_next():
            raise StopIteration
        return self.next()


# ─────────────────────────────────────────────
# Iteradores concretos
# ─────────────────────────────────────────────
class DirectoIterator(StringIterator):
    """Recorre la cadena de izquierda a derecha."""

    def __init__(self, data: str):
        self._data  = data
        self._pos   = 0

    def has_next(self) -> bool:
        return self._pos < len(self._data)

    def next(self) -> str:
        char = self._data[self._pos]
        self._pos += 1
        return char


class ReversoIterator(StringIterator):
    """Recorre la cadena de derecha a izquierda."""

    def __init__(self, data: str):
        self._data  = data
        self._pos   = len(data) - 1

    def has_next(self) -> bool:
        return self._pos >= 0

    def next(self) -> str:
        char = self._data[self._pos]
        self._pos -= 1
        return char


# ─────────────────────────────────────────────
# Colección iterable (IterableCollection)
# ─────────────────────────────────────────────
class CadenaCaracteres:
    """
    Almacena una cadena de caracteres y provee factory methods
    para obtener iteradores en ambas direcciones.
    """

    def __init__(self, cadena: str):
        self._cadena = cadena

    # ── acceso a la cadena ────────────────────
    @property
    def cadena(self) -> str:
        return self._cadena

    @cadena.setter
    def cadena(self, valor: str):
        self._cadena = valor

    # ── factory de iteradores ─────────────────
    def create_iterator_directo(self) -> DirectoIterator:
        return DirectoIterator(self._cadena)

    def create_iterator_reverso(self) -> ReversoIterator:
        return ReversoIterator(self._cadena)


# ─────────────────────────────────────────────
# Programa principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    texto = "Ingenieria de Software II"
    coleccion = CadenaCaracteres(texto)

    print("=" * 50)
    print("  Iterator — recorrido de cadena de caracteres")
    print("=" * 50)
    print(f"Cadena original: '{texto}'")
    print()

    # ── Recorrido directo ─────────────────────
    print("Recorrido DIRECTO (izquierda → derecha):")
    it_directo = coleccion.create_iterator_directo()
    resultado_d = []
    while it_directo.has_next():
        resultado_d.append(it_directo.next())
    print("  " + " ".join(resultado_d))
    print()

    # ── Recorrido reverso ─────────────────────
    print("Recorrido REVERSO (derecha → izquierda):")
    it_reverso = coleccion.create_iterator_reverso()
    resultado_r = []
    while it_reverso.has_next():
        resultado_r.append(it_reverso.next())
    print("  " + " ".join(resultado_r))
    print()

    # ── También compatible con for nativo ─────
    print("Recorrido DIRECTO usando 'for' nativo (Python):")
    salida = ""
    for c in coleccion.create_iterator_directo():
        salida += c
    print(f"  '{salida}'")

    print("=" * 50)