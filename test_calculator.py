import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_multiplicar(self):
        calc = Calculadora()
        self.assertEqual(calc.multiplicar(2, 3), 6)
        self.assertEqual(calc.multiplicar(-1, 1), -1)
        self.assertEqual(calc.multiplicar(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
