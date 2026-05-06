# TP4 - Ejercicio 4: Operaciones anidadas sobre un valor

class Number:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def print_value(self):
        print(f"Valor base: {self.value}")
        return self.value


class OperationDecorator:
    def __init__(self, number_obj):
        self._number_obj = number_obj

    def get_value(self):
        return self._number_obj.get_value()

    def print_value(self):
        result = self.get_value()
        print(f"Resultado final: {result:.2f}")
        return result


class Add2Decorator(OperationDecorator):
    def get_value(self):
        val = self._number_obj.get_value()
        return val + 2


class Multiply2Decorator(OperationDecorator):
    def get_value(self):
        val = self._number_obj.get_value()
        return val * 2


class Divide3Decorator(OperationDecorator):
    def get_value(self):
        val = self._number_obj.get_value()
        return val / 3


# Ejemplo de uso:
if __name__ == "__main__":
    num = Number(10)

    print("--- Sin agregados ---")
    num.print_value()

    print("\n--- Solo Sumar 2 ---")
    Add2Decorator(num).print_value()

    print("\n--- Sumar 2, luego Multiplicar por 2 ---")
    Multiply2Decorator(Add2Decorator(num)).print_value()

    print("\n--- Sumar 2, Multiplicar por 2, Dividir entre 3 ---")
    Divide3Decorator(Multiply2Decorator(Add2Decorator(num))).print_value()