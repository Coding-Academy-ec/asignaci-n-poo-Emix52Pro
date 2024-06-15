class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura  # Área del rectángulo: base * altura


class Circulo:
    pi = 3.141592653589793

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.pi * (self.radio ** 2)  # Área del círculo: pi * radio^2
