
class Retangulo:

    def __init__(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

    def mudaValor(self):
        self.comprimento = input('Digite um novo comprimento:')
        self.altura = input('Digite um novo valor para altura: ')

    def retornaValor(self):
        print(self.comprimento, self.altura)

    def calculaArea(self):
        return self.comprimento * self.altura

    def calculaPerimetro(self):
        return (self.comprimento + self.altura)*2

