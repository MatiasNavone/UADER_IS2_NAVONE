# TP4 - Ejercicio 5: Optimización de caracteres de texto

class CharacterStyle:
    def __init__(self, font, size, color):
        self.font = font
        self.size = size
        self.color = color

    def draw(self, char_symbol):
        print(f"Dibujar '{char_symbol}' | Estilo: Fuente={self.font}, Tamaño={self.size}, Color={self.color}")

class CharacterStyleFactory:
    _styles = {}

    @classmethod
    def get_style(cls, font, size, color):
        key = (font, size, color)
        if key not in cls._styles:
            cls._styles[key] = CharacterStyle(font, size, color)
            print(f"[Fábrica] Creando nuevo estilo: {key}")
        else:
            print(f"[Fábrica] Reutilizando estilo existente: {key}")
        return cls._styles[key]

class TextCharacter:
    def __init__(self, symbol, font, size, color):
        self.symbol = symbol
        self.style = CharacterStyleFactory.get_style(font, size, color)

    def draw(self):
        self.style.draw(self.symbol)

# Ejemplo de uso:
if __name__ == "__main__":
    print("--- Situación con Flyweight ---")
    char1 = TextCharacter("H", "Arial", 12, "Red")
    char2 = TextCharacter("o", "Arial", 12, "Red") # Reutiliza el estilo del anterior
    char3 = TextCharacter("l", "Arial", 12, "Red")
    char4 = TextCharacter("a", "Arial", 12, "Red")

    char1.draw()
    char2.draw()
    char3.draw()
    char4.draw()