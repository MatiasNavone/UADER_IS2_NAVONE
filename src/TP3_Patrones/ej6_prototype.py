# TP3 - Ejercicio 6: clonación transitiva
# Patrón: Prototype

import copy


# --- Clase Prototipo base ---

class ClasePrototipo:
    """Clase base que implementa el método clone()."""

    def __init__(self, nombre: str, datos: list):
        self.nombre = nombre
        self.datos  = datos          # atributo mutable para evidenciar deep copy

    def clone(self):
        """Retorna una copia profunda de sí misma."""
        copia = copy.deepcopy(self)
        print(f"[Prototype] '{self.nombre}' clonado → nuevo objeto id={id(copia)}")
        return copia

    def __str__(self):
        return f"<{self.__class__.__name__} nombre='{self.nombre}' datos={self.datos} id={id(self)}>"


# --- Subclase A (hereda clone) ---

class ClaseA(ClasePrototipo):
    def __init__(self, nombre: str, datos: list, extra: str = ""):
        super().__init__(nombre, datos)
        self.extra = extra          # atributo propio de ClaseA

    def __str__(self):
        return (
            f"<ClaseA nombre='{self.nombre}' datos={self.datos} "
            f"extra='{self.extra}' id={id(self)}>"
        )


# --- Subclase B (hereda clone) ---

class ClaseB(ClasePrototipo):
    def __init__(self, nombre: str, datos: list, nivel: int = 0):
        super().__init__(nombre, datos)
        self.nivel = nivel

    def __str__(self):
        return (
            f"<ClaseB nombre='{self.nombre}' datos={self.datos} "
            f"nivel={self.nivel} id={id(self)}>"
        )


# --- Demostración ---
if __name__ == "__main__":
    print("=== Original ===")
    original = ClaseA(nombre="original", datos=[1, 2, 3], extra="A")
    print(original)

    print("\n=== Clon de original (1er nivel) ===")
    clon1 = original.clone()
    clon1.nombre = "clon1"
    clon1.datos.append(4)           # modificar el clon NO afecta al original
    print(clon1)
    print(f"Original tras modificar clon1: {original}")

    print("\n=== Clon del clon (2do nivel — clonación transitiva) ===")
    clon2 = clon1.clone()
    clon2.nombre = "clon2"
    clon2.extra  = "clon de clon"
    print(clon2)
    print(f"clon1 tras modificar clon2:    {clon1}")

    print("\n=== Verificación de identidades ===")
    print(f"original is clon1 → {original is clon1}")
    print(f"clon1    is clon2 → {clon1    is clon2}")
    print(f"original.datos is clon1.datos → {original.datos is clon1.datos}")

    print("\n=== ClaseB también hereda clone() ===")
    b_original = ClaseB(nombre="avionB", datos=["ala", "turbina"], nivel=1)
    b_clon     = b_original.clone()
    b_clon.nombre = "avionB_clon"
    b_clon.nivel  = 2
    print(f"  Original: {b_original}")
    print(f"  Clon:     {b_clon}")