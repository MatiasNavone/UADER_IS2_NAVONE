# TP4 - Ejercicio 2: Producción de láminas de acero

from abc import ABC, abstractmethod

class MillImplementation(ABC):
    @abstractmethod
    def produce(self, thickness, width) -> str:
        pass

class Mill5Meters(MillImplementation):
    def produce(self, thickness, width) -> str:
        return f"Lámina de {thickness}\" de espesor y {width} metros de ancho producida en tren de 5 metros."

class Mill10Meters(MillImplementation):
    def produce(self, thickness, width) -> str:
        return f"Lámina de {thickness}\" de espesor y {width} metros de ancho producida en tren de 10 metros."

class SteelSheetProduct:
    def __init__(self, thickness: float, width: float, mill: MillImplementation):
        self.thickness = thickness
        self.width = width
        self.mill = mill

    def change_mill(self, mill: MillImplementation):
        self.mill = mill

    def run_production(self):
        result = self.mill.produce(self.thickness, self.width)
        print(f"Producción en curso: {result}")

# Ejemplo de uso:
if __name__ == "__main__":
    sheet = SteelSheetProduct(0.5, 1.5, Mill5Meters())
    sheet.run_production()

    # Cambiar de tren laminador dinámicamente
    sheet.change_mill(Mill10Meters())
    sheet.run_production()