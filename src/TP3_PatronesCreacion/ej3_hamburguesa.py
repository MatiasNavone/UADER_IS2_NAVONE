# TP3 - Ejercicio 3: hamburguesa con método de entrega
# Patrón: Builder

from abc import ABC, abstractmethod

class Hamburguesa:
    """Producto final construido por el Builder."""

    def __init__(self):
        self.nombre          = "Hamburguesa"
        self.metodo_entrega  = None

    def describir(self):
        print(f"\n=== Pedido: {self.nombre} ===")
        print(f"  Método de entrega: {self.metodo_entrega}")


# --- Builder (interfaz) ---

class HamburguesaBuilder(ABC):

    def __init__(self):
        self._hamburguesa = Hamburguesa()

    def obtener_resultado(self) -> Hamburguesa:
        return self._hamburguesa

    @abstractmethod
    def set_metodo_entrega(self):
        pass


# --- Builders concretos ---

class HamburguesaMostrador(HamburguesaBuilder):
    def set_metodo_entrega(self):
        self._hamburguesa.metodo_entrega = "Entrega en mostrador"


class HamburguesaRetiro(HamburguesaBuilder):
    def set_metodo_entrega(self):
        self._hamburguesa.metodo_entrega = "Retiro por el cliente"


class HamburguesaDelivery(HamburguesaBuilder):
    def set_metodo_entrega(self):
        self._hamburguesa.metodo_entrega = "Envío por delivery"


# --- Director ---

class Cocina:
    """Director: coordina los pasos de construcción usando un Builder."""

    def __init__(self, builder: HamburguesaBuilder):
        self._builder = builder

    def preparar_pedido(self) -> Hamburguesa:
        self._builder.set_metodo_entrega()
        return self._builder.obtener_resultado()


# --- Demostración ---
if __name__ == "__main__":
    pedidos = [
        HamburguesaMostrador(),
        HamburguesaRetiro(),
        HamburguesaDelivery(),
    ]

    for builder in pedidos:
        cocina = Cocina(builder)
        hamburguesa = cocina.preparar_pedido()
        hamburguesa.describir()