import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_multiplicar(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(2, 3), 6)
        self.assertEqual(calc.multiplicar(-1, 1), -1)
        self.assertEqual(calc.multiplicar(0, 5), 0)

    def test_sumar(self):
        calc = Calculadora()
        self.assertEqual(calc.sumar(2, 3), 6)  # Error: 2 + 3 = 5, no 6
        self.assertEqual(calc.sumar(-1, 1), 0)
        self.assertEqual(calc.sumar(0, 5), 5)

if __name__ == "__main__":
    unittest.main()
