# TP3 - Ejercicio 7: Abstract Factory
# Situación: Una aplicación de escritorio debe generar componentes de interfaz
# gráfica (botón, checkbox, campo de texto) compatibles con el sistema operativo
# donde se ejecuta (Windows o Linux/GTK).
#
# El código cliente no necesita saber qué SO está corriendo; simplemente
# solicita componentes a la fábrica y estos son siempre compatibles entre sí.
#
# Patrón: Abstract Factory
# ─────────────────────────────────────────────────────────────────────────────

from abc import ABC, abstractmethod
import platform


# --- Interfaces de productos ---

class Boton(ABC):
    @abstractmethod
    def render(self): pass

class Checkbox(ABC):
    @abstractmethod
    def render(self): pass

class CampoTexto(ABC):
    @abstractmethod
    def render(self): pass


# --- Familia Windows ---

class BotonWindows(Boton):
    def render(self):
        print("  [Windows] Renderizando botón  ▶ estilo Win32/WinForms")

class CheckboxWindows(Checkbox):
    def render(self):
        print("  [Windows] Renderizando checkbox ▶ estilo Win32/WinForms")

class CampoTextoWindows(CampoTexto):
    def render(self):
        print("  [Windows] Renderizando campo de texto ▶ estilo Win32/WinForms")


# --- Familia GTK (Linux) ---

class BotonGTK(Boton):
    def render(self):
        print("  [GTK]     Renderizando botón  ▶ estilo GTK3/GNOME")

class CheckboxGTK(Checkbox):
    def render(self):
        print("  [GTK]     Renderizando checkbox ▶ estilo GTK3/GNOME")

class CampoTextoGTK(CampoTexto):
    def render(self):
        print("  [GTK]     Renderizando campo de texto ▶ estilo GTK3/GNOME")


# --- Abstract Factory ---

class UIFactory(ABC):
    @abstractmethod
    def crear_boton(self)       -> Boton:     pass

    @abstractmethod
    def crear_checkbox(self)    -> Checkbox:  pass

    @abstractmethod
    def crear_campo_texto(self) -> CampoTexto: pass


# --- Factories concretas ---

class WindowsUIFactory(UIFactory):
    def crear_boton(self)       -> Boton:      return BotonWindows()
    def crear_checkbox(self)    -> Checkbox:   return CheckboxWindows()
    def crear_campo_texto(self) -> CampoTexto: return CampoTextoWindows()

class GTKUIFactory(UIFactory):
    def crear_boton(self)       -> Boton:      return BotonGTK()
    def crear_checkbox(self)    -> Checkbox:   return CheckboxGTK()
    def crear_campo_texto(self) -> CampoTexto: return CampoTextoGTK()


# --- Selector de fábrica según SO (decisión en runtime) ---

def obtener_factory() -> UIFactory:
    so = platform.system()
    if so == "Windows":
        print(f"[AbstractFactory] SO detectado: Windows → usando WindowsUIFactory\n")
        return WindowsUIFactory()
    else:
        print(f"[AbstractFactory] SO detectado: {so} → usando GTKUIFactory\n")
        return GTKUIFactory()


# --- Código cliente --- 

def construir_formulario(factory: UIFactory):
    """El cliente sólo conoce la interfaz; no sabe qué SO hay debajo."""
    print("=== Construyendo formulario de login ===")
    factory.crear_campo_texto().render()   # usuario
    factory.crear_campo_texto().render()   # contraseña
    factory.crear_checkbox().render()      # "recordarme"
    factory.crear_boton().render()         # botón "ingresar"
    print()


# --- Demostración ---
if __name__ == "__main__":
    # Uso automático (detecta el SO real)
    factory = obtener_factory()
    construir_formulario(factory)

    # Forzar ambas familias para mostrar diferencia
    print("--- Forzando familia Windows ---")
    construir_formulario(WindowsUIFactory())

    print("--- Forzando familia GTK ---")
    construir_formulario(GTKUIFactory())