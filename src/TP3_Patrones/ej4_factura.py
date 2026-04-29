# TP3 - Ejercicio 4: Factura según condición impositiva del cliente
# Patrón: Factory

from abc import ABC, abstractmethod


# --- Producto base ---

class Factura(ABC):

    def __init__(self, importe: float):
        self.importe = importe

    @abstractmethod
    def describir(self):
        pass


# --- Productos concretos ---

class FacturaTipoA(Factura):
    """Para clientes IVA Responsable Inscripto."""

    def describir(self):
        print(f"\n┌─────────────────────────────────────┐")
        print(f"│          FACTURA  TIPO  A            │")
        print(f"│  Condición: IVA Responsable          │")
        print(f"│  Total: ${self.importe:>10.2f}               │")
        print(f"└─────────────────────────────────────┘")


class FacturaTipoB(Factura):
    """Para clientes IVA No Inscripto / Consumidor Final."""

    def describir(self):
        print(f"\n┌─────────────────────────────────────┐")
        print(f"│          FACTURA  TIPO  B            │")
        print(f"│  Condición: IVA No Inscripto         │")
        print(f"│  Total: ${self.importe:>10.2f}               │")
        print(f"└─────────────────────────────────────┘")


class FacturaTipoC(Factura):
    """Para clientes IVA Exento / Monotributista."""

    def describir(self):
        print(f"\n┌─────────────────────────────────────┐")
        print(f"│          FACTURA  TIPO  C            │")
        print(f"│  Condición: IVA Exento               │")
        print(f"│  Total: ${self.importe:>10.2f}               │")
        print(f"└─────────────────────────────────────┘")


# --- Factory ---

class FacturaFactory:

    CONDICIONES = {
        "responsable": FacturaTipoA,
        "no_inscripto": FacturaTipoB,
        "exento": FacturaTipoC,
    }

    @staticmethod
    def crear(condicion_impositiva: str, importe: float) -> Factura:
        clave = condicion_impositiva.lower().replace(" ", "_")
        clase = FacturaFactory.CONDICIONES.get(clave)
        if clase is None:
            raise ValueError(
                f"Condición impositiva desconocida: '{condicion_impositiva}'. "
                f"Opciones válidas: {list(FacturaFactory.CONDICIONES.keys())}"
            )
        return clase(importe)


# --- Demostración ---
if __name__ == "__main__":
    casos = [
        ("responsable",  15000.00),
        ("no_inscripto",  8500.50),
        ("exento",        3200.75),
    ]

    for condicion, monto in casos:
        factura = FacturaFactory.crear(condicion, monto)
        factura.describir()