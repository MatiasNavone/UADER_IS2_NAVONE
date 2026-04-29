# TP3 - Ejercicio 5: Avión
# Patrón: Builder

from abc import ABC, abstractmethod


# --- Producto ---

class Avion:
    def __init__(self):
        self.body             = None
        self.turbinas         = []
        self.alas             = []
        self.tren_aterrizaje  = None

    def __str__(self):
        return (
            f"\n=== Avión ensamblado ===\n"
            f"  Body:            {self.body}\n"
            f"  Turbinas:        {', '.join(self.turbinas)}\n"
            f"  Alas:            {', '.join(self.alas)}\n"
            f"  Tren aterrizaje: {self.tren_aterrizaje}\n"
        )


# --- Builder (interfaz) ---

class AvionBuilder(ABC):

    def __init__(self):
        self._avion = Avion()

    def obtener_avion(self) -> Avion:
        return self._avion

    @abstractmethod
    def construir_body(self):
        pass

    @abstractmethod
    def construir_turbinas(self):
        pass

    @abstractmethod
    def construir_alas(self):
        pass

    @abstractmethod
    def construir_tren_aterrizaje(self):
        pass


# --- Builder concreto: Avión Comercial ---

class AvionComercialBuilder(AvionBuilder):

    def construir_body(self):
        self._avion.body = "Fuselaje ancho (wide-body) - Aluminio reforzado"

    def construir_turbinas(self):
        self._avion.turbinas = [
            "Turbina izquierda CFM56-5B",
            "Turbina derecha CFM56-5B",
        ]

    def construir_alas(self):
        self._avion.alas = [
            "Ala izquierda con winglet",
            "Ala derecha con winglet",
        ]

    def construir_tren_aterrizaje(self):
        self._avion.tren_aterrizaje = "Tren triciclo retráctil - 6 ruedas"


    # ── Builder concreto: Avión de Combate ───────────────────────────────────────

class AvionCombateBuilder(AvionBuilder):

    def construir_body(self):
        self._avion.body = "Fuselaje estrecho - Titanio/composites furtivos"

    def construir_turbinas(self):
        self._avion.turbinas = [
            "Turbina izquierda GE F110 con postquemador",
            "Turbina derecha GE F110 con postquemador",
        ]

    def construir_alas(self):
        self._avion.alas = [
            "Ala izquierda en delta con flap",
            "Ala derecha en delta con flap",
        ]

    def construir_tren_aterrizaje(self):
        self._avion.tren_aterrizaje = "Tren biciclo reforzado para portaaviones"


# --- Director ---

class Hangar:
    """Director: ensambla el avión siguiendo los pasos del Builder."""

    def __init__(self, builder: AvionBuilder):
        self._builder = builder

    def ensamblar(self) -> Avion:
        self._builder.construir_body()
        self._builder.construir_turbinas()
        self._builder.construir_alas()
        self._builder.construir_tren_aterrizaje()
        return self._builder.obtener_avion()


# --- Demostración ---
if __name__ == "__main__":
    print("--- Construyendo Avión Comercial ---")
    hangar1 = Hangar(AvionComercialBuilder())
    avion_comercial = hangar1.ensamblar()
    print(avion_comercial)

    print("--- Construyendo Avión de Combate ---")
    hangar2 = Hangar(AvionCombateBuilder())
    avion_combate = hangar2.ensamblar()
    print(avion_combate)