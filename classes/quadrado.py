class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def mudaValor(self):
        self.lado = int(input('Digite um novo valor para o lado:'))

    def calculaArea(self):
        area = self.lado * self.lado
        return area

q1 = Quadrado(4)

q1.mudaValor()

print(q1.lado)

print(q1.calculaArea())
