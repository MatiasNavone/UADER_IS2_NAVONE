"""
TP - Patrones de Comportamiento
Punto 3: Observer
- Publisher (EventManager) emite IDs de 4 caracteres.
- Cada Subscriber tiene su propio ID y reacciona únicamente
  cuando el ID emitido coincide con el suyo.
- Se implementan 4 clases suscriptoras con IDs distintos.
- Se emiten 8 IDs, asegurando al menos 4 coincidencias.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# ─────────────────────────────────────────────
# Interfaz Subscriber
# ─────────────────────────────────────────────
class Subscriber(ABC):
    """Interfaz común de todos los suscriptores."""

    @abstractmethod
    def update(self, id_emitido: str) -> None:
        """Recibe el ID emitido por el Publisher."""
        ...

    @property
    @abstractmethod
    def subscriber_id(self) -> str:
        """Devuelve el ID propio del suscriptor."""
        ...


# ─────────────────────────────────────────────
# Publisher / EventManager
# ─────────────────────────────────────────────
class EventManager:
    """
    Gestor de eventos.
    Mantiene la lista de suscriptores y notifica a todos
    cuando se emite un nuevo ID.
    """

    def __init__(self):
        self._subscribers: List[Subscriber] = []

    def subscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.append(subscriber)
        print(f"[EventManager] Suscriptor registrado: ID='{subscriber.subscriber_id}'")

    def unsubscribe(self, subscriber: Subscriber) -> None:
        self._subscribers.remove(subscriber)

    def notify(self, id_emitido: str) -> None:
        """Emite el ID a todos los suscriptores registrados."""
        print(f"\n[EventManager] ── Emitiendo ID: '{id_emitido}' ──")
        for sub in self._subscribers:
            sub.update(id_emitido)


# ─────────────────────────────────────────────
# Suscriptores concretos (4 clases con IDs fijos)
# ─────────────────────────────────────────────
class SuscriptorAlfa(Subscriber):
    """Suscriptor con ID 'ALFA'."""
    _ID = "ALFA"

    @property
    def subscriber_id(self) -> str:
        return self._ID

    def update(self, id_emitido: str) -> None:
        if id_emitido == self._ID:
            print(f"  [SuscriptorAlfa] ¡ID '{id_emitido}' coincide! → Procesando evento.")


class SuscriptorBeta(Subscriber):
    """Suscriptor con ID 'BETA'."""
    _ID = "BETA"

    @property
    def subscriber_id(self) -> str:
        return self._ID

    def update(self, id_emitido: str) -> None:
        if id_emitido == self._ID:
            print(f"  [SuscriptorBeta] ¡ID '{id_emitido}' coincide! → Procesando evento.")


class SuscriptorGama(Subscriber):
    """Suscriptor con ID 'GAMA'."""
    _ID = "GAMA"

    @property
    def subscriber_id(self) -> str:
        return self._ID

    def update(self, id_emitido: str) -> None:
        if id_emitido == self._ID:
            print(f"  [SuscriptorGama] ¡ID '{id_emitido}' coincide! → Procesando evento.")


class SuscriptorDelta(Subscriber):
    """Suscriptor con ID 'DELT'."""
    _ID = "DELT"

    @property
    def subscriber_id(self) -> str:
        return self._ID

    def update(self, id_emitido: str) -> None:
        if id_emitido == self._ID:
            print(f"  [SuscriptorDelta] ¡ID '{id_emitido}' coincide! → Procesando evento.")


# ─────────────────────────────────────────────
# Programa principal
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  Observer — notificación por coincidencia de ID")
    print("=" * 55)

    # Crear y registrar los 4 suscriptores
    manager = EventManager()
    manager.subscribe(SuscriptorAlfa())
    manager.subscribe(SuscriptorBeta())
    manager.subscribe(SuscriptorGama())
    manager.subscribe(SuscriptorDelta())

    print()
    print("─" * 55)
    print("Emitiendo 8 IDs (4 coincidentes + 4 no coincidentes):")
    print("─" * 55)

    # 8 IDs: los 4 propios (garantizan coincidencia) + 4 que no coinciden
    ids_a_emitir = [
        "ALFA",   # coincide con SuscriptorAlfa
        "BETA",   # coincide con SuscriptorBeta
        "XYZW",   # no coincide con nadie
        "GAMA",   # coincide con SuscriptorGama
        "DELT",   # coincide con SuscriptorDelta
        "AAAA",   # no coincide con nadie
        "ZZZZ",   # no coincide con nadie
        "1234",   # no coincide con nadie
    ]

    for id_emitido in ids_a_emitir:
        manager.notify(id_emitido)

    print()
    print("=" * 55)
    print("Fin de la emisión de IDs.")
    print("=" * 55)