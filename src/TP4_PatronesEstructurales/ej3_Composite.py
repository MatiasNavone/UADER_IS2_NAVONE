# TP4 - Ejercicio 3: Ensamblados y piezas jerárquicas

from abc import ABC, abstractmethod

class AssemblyComponent(ABC):
    @abstractmethod
    def display(self, depth=0):
        pass

class Part(AssemblyComponent):
    def __init__(self, name):
        self.name = name

    def display(self, depth=0):
        print("  " * depth + f"⚙️ Pieza: {self.name}")

class SubAssembly(AssemblyComponent):
    def __init__(self, name):
        self.name = name
        self._children = []

    def add(self, component: AssemblyComponent):
        self._children.append(component)

    def remove(self, component: AssemblyComponent):
        self._children.remove(component)

    def display(self, depth=0):
        print("  " * depth + f"📦 Subconjunto: {self.name}")
        for child in self._children:
            child.display(depth + 1)

# Ejemplo de uso:
if __name__ == "__main__":
    main_product = SubAssembly("Producto Principal")

    # 3 sub-conjuntos con 4 piezas cada uno
    for i in range(1, 4):
        sub = SubAssembly(f"Sub-conjunto {i}")
        for j in range(1, 5):
            sub.add(Part(f"Pieza {i}.{j}"))
        main_product.add(sub)

    print("--- Configuración inicial ---")
    main_product.display()

    # Agregar sub-conjunto opcional adicional con 4 piezas
    optional_sub = SubAssembly("Sub-conjunto Opcional")
    for j in range(1, 5):
        optional_sub.add(Part(f"Pieza Opcional.{j}"))
    main_product.add(optional_sub)

    print("\n--- Configuración actualizada con elemento opcional ---")
    main_product.display()