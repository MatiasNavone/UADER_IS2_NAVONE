"""
test_functional.py - Tests funcionales para rpn.py
Ejecuta el programa como proceso externo y verifica su salida,
simulando el uso real desde la línea de comandos.
"""
import unittest
import subprocess
import sys
import os

# Ruta al intérprete Python activo y al programa bajo prueba
PYTHON  = sys.executable
PROGRAM = os.path.join(os.path.dirname(__file__), "rpn.py")


def run_rpn(*args):
    """
    Ejecuta rpn.py con los argumentos dados y retorna (stdout, stderr, returncode).
    Ejemplo: run_rpn("3", "4", "+") simula: python rpn.py 3 4 +
    """
    result = subprocess.run(
        [PYTHON, PROGRAM] + list(args),
        capture_output=True, text=True
    )
    return result.stdout.strip(), result.stderr.strip(), result.returncode


class TestFunctionalBasicOps(unittest.TestCase):
    """Casos funcionales: operaciones aritméticas básicas."""

    def test_suma_enteros(self):
        """TC-F01: 3 4 + debe retornar 7"""
        out, _, code = run_rpn("3", "4", "+")
        self.assertEqual(code, 0)
        self.assertEqual(out, "7")

    def test_resta(self):
        """TC-F02: 10 3 - debe retornar 7"""
        out, _, code = run_rpn("10", "3", "-")
        self.assertEqual(code, 0)
        self.assertEqual(out, "7")

    def test_multiplicacion(self):
        """TC-F03: 3 4 * debe retornar 12"""
        out, _, code = run_rpn("3", "4", "*")
        self.assertEqual(code, 0)
        self.assertEqual(out, "12")

    def test_division(self):
        """TC-F04: 10 4 / debe retornar 2.5"""
        out, _, code = run_rpn("10", "4", "/")
        self.assertEqual(code, 0)
        self.assertIn("2.5", out)

    def test_expresion_encadenada(self):
        """TC-F05: 5 1 2 + 4 * + 3 - debe retornar 14"""
        out, _, code = run_rpn("5", "1", "2", "+", "4", "*", "+", "3", "-")
        self.assertEqual(code, 0)
        self.assertEqual(out, "14")

    def test_expresion_encadenada_2(self):
        """TC-F06: 2 3 4 * + debe retornar 14"""
        out, _, code = run_rpn("2", "3", "4", "*", "+")
        self.assertEqual(code, 0)
        self.assertEqual(out, "14")

    def test_operandos_negativos(self):
        """TC-F07: -3 -4 * debe retornar 12"""
        out, _, code = run_rpn("-3", "-4", "*")
        self.assertEqual(code, 0)
        self.assertEqual(out, "12")

    def test_floats(self):
        """TC-F08: 1.5 2.5 + debe retornar 4.0"""
        out, _, code = run_rpn("1.5", "2.5", "+")
        self.assertEqual(code, 0)
        self.assertEqual(out, "4")


class TestFunctionalConstants(unittest.TestCase):
    """Casos funcionales: constantes matemáticas."""

    def test_pi(self):
        """TC-F09: p debe retornar pi (~3.14159)"""
        out, _, code = run_rpn("p")
        self.assertEqual(code, 0)
        self.assertIn("3.14159", out)

    def test_euler(self):
        """TC-F10: e debe retornar e (~2.71828)"""
        out, _, code = run_rpn("e")
        self.assertEqual(code, 0)
        self.assertIn("2.71828", out)

    def test_phi(self):
        """TC-F11: j debe retornar phi (~1.61803)"""
        out, _, code = run_rpn("j")
        self.assertEqual(code, 0)
        self.assertIn("1.61803", out)


class TestFunctionalMathFunctions(unittest.TestCase):
    """Casos funcionales: funciones matemáticas."""

    def test_sqrt(self):
        """TC-F12: 9 sqrt debe retornar 3"""
        out, _, code = run_rpn("9", "sqrt")
        self.assertEqual(code, 0)
        self.assertEqual(out, "3")

    def test_log(self):
        """TC-F13: 100 log debe retornar 2"""
        out, _, code = run_rpn("100", "log")
        self.assertEqual(code, 0)
        self.assertEqual(out, "2")

    def test_ln(self):
        """TC-F14: 1 ln debe retornar 0"""
        out, _, code = run_rpn("1", "ln")
        self.assertEqual(code, 0)
        self.assertEqual(out, "0")

    def test_chs(self):
        """TC-F15: 5 chs debe retornar -5"""
        out, _, code = run_rpn("5", "chs")
        self.assertEqual(code, 0)
        self.assertEqual(out, "-5")

    def test_inverso(self):
        """TC-F16: 4 1/x debe retornar 0.25"""
        out, _, code = run_rpn("4", "1/x")
        self.assertEqual(code, 0)
        self.assertIn("0.25", out)


class TestFunctionalTrig(unittest.TestCase):
    """Casos funcionales: funciones trigonométricas en grados."""

    def test_sin_90(self):
        """TC-F17: 90 sin debe retornar 1"""
        out, _, code = run_rpn("90", "sin")
        self.assertEqual(code, 0)
        self.assertEqual(out, "1")

    def test_cos_0(self):
        """TC-F18: 0 cos debe retornar 1"""
        out, _, code = run_rpn("0", "cos")
        self.assertEqual(code, 0)
        self.assertEqual(out, "1")

    def test_tg_45(self):
        """TC-F19: 45 tg debe retornar ~1.0 (tolerancia por punto flotante)"""
        out, _, code = run_rpn("45", "tg")
        self.assertEqual(code, 0)
        self.assertAlmostEqual(float(out), 1.0, places=5)

    def test_asin(self):
        """TC-F20: 1 asin debe retornar 90"""
        out, _, code = run_rpn("1", "asin")
        self.assertEqual(code, 0)
        self.assertEqual(out, "90")


class TestFunctionalStackCommands(unittest.TestCase):
    """Casos funcionales: comandos de pila."""

    def test_dup(self):
        """TC-F21: 3 dup + debe retornar 6 (duplica y suma)"""
        out, _, code = run_rpn("3", "dup", "+")
        self.assertEqual(code, 0)
        self.assertEqual(out, "6")

    def test_swap(self):
        """TC-F22: 10 3 swap - debe retornar -7 (invierte orden)"""
        out, _, code = run_rpn("10", "3", "swap", "-")
        self.assertEqual(code, 0)
        self.assertEqual(out, "-7")

    def test_drop(self):
        """TC-F23: 5 99 drop debe retornar 5 (descarta tope)"""
        out, _, code = run_rpn("5", "99", "drop")
        self.assertEqual(code, 0)
        self.assertEqual(out, "5")

    def test_clear(self):
        """TC-F24: 9 8 7 clear 42 debe retornar 42 (limpia y empuja)"""
        out, _, code = run_rpn("9", "8", "7", "clear", "42")
        self.assertEqual(code, 0)
        self.assertEqual(out, "42")


class TestFunctionalMemory(unittest.TestCase):
    """Casos funcionales: memoria STO/RCL."""

    def test_sto_rcl(self):
        """TC-F25: 42 sto 05 8 rcl 05 + debe retornar 50"""
        out, _, code = run_rpn("42", "sto", "05", "8", "rcl", "05", "+")
        self.assertEqual(code, 0)
        self.assertEqual(out, "50")

    def test_rcl_default(self):
        """TC-F26: rcl 00 debe retornar 0 (valor inicial de memoria)"""
        out, _, code = run_rpn("rcl", "00")
        self.assertEqual(code, 0)
        self.assertEqual(out, "0")


class TestFunctionalErrors(unittest.TestCase):
    """Casos funcionales: manejo de errores — exit code != 0 y mensaje en stderr."""

    def test_division_por_cero(self):
        """TC-F27: 3 0 / debe fallar con mensaje de error"""
        _, err, code = run_rpn("3", "0", "/")
        self.assertNotEqual(code, 0)
        self.assertIn("Error", err)

    def test_token_invalido(self):
        """TC-F28: token desconocido debe fallar con mensaje de error"""
        _, err, code = run_rpn("3", "4", "foo")
        self.assertNotEqual(code, 0)
        self.assertIn("Error", err)

    def test_pila_insuficiente(self):
        """TC-F29: operación con pila vacía debe fallar"""
        _, err, code = run_rpn("3", "+")
        self.assertNotEqual(code, 0)
        self.assertIn("Error", err)

    def test_demasiados_valores(self):
        """TC-F30: expresión con más de 1 resultado debe fallar"""
        _, err, code = run_rpn("3", "4")
        self.assertNotEqual(code, 0)
        self.assertIn("Error", err)

    def test_sqrt_negativo(self):
        """TC-F31: sqrt de número negativo debe fallar"""
        _, err, code = run_rpn("-1", "sqrt")
        self.assertNotEqual(code, 0)
        self.assertIn("Error", err)

    def test_slot_invalido(self):
        """TC-F32: slot de memoria fuera de rango debe fallar"""
        _, err, code = run_rpn("5", "sto", "99")
        self.assertNotEqual(code, 0)
        self.assertIn("Error", err)


if __name__ == "__main__":
    unittest.main(verbosity=2)
