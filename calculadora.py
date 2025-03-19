class Calculadora:
    def multiplicar(self, a, b):
        return a * b


    def sumar(self, a, b):
        return a + b

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py <num1> <num2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        calc = Calculadora()
        resultado_multiplicacion = calc.multiplicar(num1, num2)
        resultado_suma = calc.sumar(num1, num2)
        print(f"El resultado de {num1} * {num2} es: {resultado_multiplicacion}")
        print(f"El resultado de {num1} + {num2} es: {resultado_suma}")
    except ValueError:
        print("Error: Los argumentos deben ser números.")
