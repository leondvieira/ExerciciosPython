from graphics import *

janela = GraphWin('Teste', 840, 600)

circ = Circle(Point(200,200), 190)
circ.setFill('yellow')
circ.draw(janela)


circ = Circle(Point(65, 60), 30)
circ.setFill('white')
circ.draw(janela)

circ1 = Circle(Point(135, 60), 30)
circ1.setFill('white')
circ1.draw(janela)

olho_direita = Circle(Point(140, 40), 10)
olho_direita.setFill('black')
olho_direita.draw(janela)

olho_esquerda = Circle(Point(60, 40), 10)
olho_esquerda.setFill('black')
olho_esquerda.draw(janela)

boca = Image(Point(120, 200), 'boca1.png')
boca.draw(janela)


a = input('AA')