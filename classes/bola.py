class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circuferencia = circunferencia
        self.material = material

    def trocaCor(self):
        self.cor = input('Nova Cor: ')

    def mostraCor(self):
        return print(self.cor)

b1 = Bola('amarelo', 20, 'metal')

b1.mostraCor()
b1.trocaCor()
b1.mostraCor()
