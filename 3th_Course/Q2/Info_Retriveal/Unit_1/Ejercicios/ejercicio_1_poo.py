class Calculadora:
    """Clase para realizar operaciones matemáticas básicas."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def sumar(self) -> float:
        return self.a + self.b

    def restar(self) -> float:
        return self.a - self.b

    def multiplicar(self) -> float:
        return self.a * self.b

    def dividir(self) -> float:
        try:
            return self.a / self.b
        except ZeroDivisionError:
            print("Error: ¡No se puede dividir por cero!")
            return float('NaN')

if __name__ == "__main__":
    calc = Calculadora(10, 5)
    print(f"Suma: {calc.sumar()}")
    print(f"Resta: {calc.restar()}")
    print(f"Multiplicación: {calc.multiplicar()}")
    print(f"División: {calc.dividir()}")
    
    # Prueba de error
    calc_nula = Calculadora(10, 0)
    print(f"División por cero: {calc_nula.dividir()}")
