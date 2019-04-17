#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@ifc-araquari.edu.br>
# Lista de exercícios 2.2

import math


def duzias(ovos):
    ''' Receba o número de ovos e devolva a quantidade de dúzias
    correspondente. Considere sempre dúzias cheias, arredondando pra
    cima se necessário.
    '''

    if ovos <= 0:
        pass
    elif (ovos % 12) == 0:
        return ovos // 12
    else:
        caixas = ovos // 12
        return caixas + 1


def baskara(a, b, c):
    '''Calcule as raízes de uma equação do segundo grau, na forma
    ax2 + bx + c. A função recebe a, b e c e faz as consistências,
    informando ao usuário nas seguintes situações:
    - Se o usuário informar o valor de A igual a zero é uma equaçao do
    2o grau.
    - Se o delta calculado for negativo, a equação não possui raizes reais.
    Devolva uma tupla vazia.
    - Se o delta calculado for igual a zero a equação possui apenas uma
    raiz real. Devolva uma tupla com um único valor.
    - Se o delta for positivo, a equação possui duas raiz reais.
    Devolva uma tupla com dois elementos.
    '''

    if a == 0:
        x = (c / b) * -1
        return (x,)
    else:
        delta = (b**2) - (4 * a * c)

        if delta < 0:
            return ()
        elif delta > 0:
            x1 = (b*(-1) + (delta**0.5)) / 2 * a
            x2 = (b*(-1) - (delta**0.5)) / 2 * a

            return (x1,x2)
        elif delta == 0:
            x1 = (b*(-1) + (delta**0.5)) / 2 * a
            return (x1,)

def decompor_numero(numero):
    '''
    Leia um número inteiro menor que 1000 e devolva a quantidade de
    centenas, dezenas e unidades do mesmo.
    Obs.: não utilize operações com strings
    '''

    if numero < 1000:
        centenas = numero // 100
        dezenas = (numero % 100) // 10
        unidades = (numero % 100) % 10
        return (centenas,dezenas,unidades)
    else:
        return ()

def caixa_eletronico(valor):
    '''Receba a valor do saque e retorne uma lista de pares de valores,
    correspondentes ao valor das notas e quantidades de notas.
    As notas disponíveis serão as de 1, 5, 10, 25, 50 e 100 reais.
    O valor é máximo de 600 reais, sem valor minimo.
    Não se preocupe com a quantidade de notas existentes na máquina.
    Procure dar sempre o número mínimo de notas, partindo das maiores
    para as menores.
    '''
    
    saque = []

    if valor <= 600:
        qnt_nota100 = valor // 100
        qnt_nota50 = (valor % 100) // 50
        qnt_nota25 = ((valor % 100) % 50) // 25
        qnt_nota10 = (((valor % 100) % 50) % 25) // 10
        qnt_nota5 = ((((valor % 100) % 50) % 25) % 10) // 5
        qnt_nota1 = (((((valor % 100) % 50) % 25) % 10) % 5) // 1

        if qnt_nota100 != 0:
            saque.append((100,qnt_nota100))
        if qnt_nota50 != 0:
            saque.append((50,qnt_nota50))
        if qnt_nota25 != 0:
            saque.append((25,qnt_nota25))
        if qnt_nota10 != 0:
            saque.append((10,qnt_nota10))
        if qnt_nota5 != 0:
            saque.append((5,qnt_nota5))
        if qnt_nota1 != 0:
            saque.append((1,qnt_nota1))
        return saque

    else:
        return []

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % ('Falhou')
    else:
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    print('Dúzias:')
    test(duzias(12), 1)
    test(duzias(24), 2)
    test(duzias(11), 1)
    test(duzias(23), 2)
    test(duzias(25), 3)

    print('Báskara:')
    test(baskara(1, 4, 4), (-2.0,))
    test(baskara(1, 5, 4), (-1.0, -4.0))
    test(baskara(0, 4, 2), (-0.5,))
    test(baskara(4, 4, 4), ())

    print('Decompor número:')
    test(decompor_numero(2016), ())
    test(decompor_numero(326), (3, 2, 6))
    test(decompor_numero(320), (3, 2, 0))
    test(decompor_numero(310), (3, 1, 0))
    test(decompor_numero(305), (3, 0, 5))
    test(decompor_numero(300), (3, 0, 0))
    test(decompor_numero(100), (1, 0, 0))
    test(decompor_numero(101), (1, 0, 1))
    test(decompor_numero(311), (3, 1, 1))
    test(decompor_numero(111), (1, 1, 1))
    test(decompor_numero(12), (0, 1, 2))
    test(decompor_numero(25), (0, 2, 5))
    test(decompor_numero(20), (0, 2, 0))
    test(decompor_numero(10), (0, 1, 0))
    test(decompor_numero(21), (0, 2, 1))
    test(decompor_numero(11), (0, 1, 1))
    test(decompor_numero(16), (0, 1, 6))
    test(decompor_numero(1), (0, 0, 1))
    test(decompor_numero(7), (0, 0, 7))

    print('Caixa eletrônico:')
    test(caixa_eletronico(100), [(100, 1)])
    test(caixa_eletronico(200), [(100, 2)])
    test(caixa_eletronico(150), [(100, 1), (50, 1)])
    test(caixa_eletronico(50), [(50, 1)])
    test(caixa_eletronico(175), [(100, 1), (50, 1), (25, 1)])
    test(caixa_eletronico(75), [(50, 1), (25, 1)])
    test(caixa_eletronico(125), [(100, 1), (25, 1)])
    test(caixa_eletronico(25), [(25, 1)])
    test(caixa_eletronico(250), [(100, 2), (50, 1)])
    test(caixa_eletronico(10), [(10, 1)])
    test(caixa_eletronico(20), [(10, 2)])
    test(caixa_eletronico(110), [(100, 1), (10, 1)])
    test(caixa_eletronico(120), [(100, 1), (10, 2)])
    test(caixa_eletronico(60), [(50, 1), (10, 1)])
    test(caixa_eletronico(70), [(50, 1), (10, 2)])
    test(caixa_eletronico(35), [(25, 1), (10, 1)])
    test(caixa_eletronico(135), [(100, 1), (25, 1), (10, 1)])
    test(caixa_eletronico(160), [(100, 1), (50, 1), (10, 1)])
    test(caixa_eletronico(165), [(100, 1), (50, 1), (10, 1), (5, 1)])
    test(caixa_eletronico(65), [(50, 1), (10, 1), (5, 1)])
    test(caixa_eletronico(115), [(100, 1), (10, 1), (5, 1)])
    test(caixa_eletronico(5), [(5, 1)])
    test(caixa_eletronico(6), [(5, 1), (1, 1)])
    test(caixa_eletronico(191), [(100, 1), (50, 1), (25, 1), (10, 1), (5, 1), (1, 1)])
    test(caixa_eletronico(0), [])
    test(caixa_eletronico(600), [(100, 6)])
    test(caixa_eletronico(601), [])
    test(caixa_eletronico(599), [(100, 5), (50, 1), (25, 1), (10, 2), (1, 4)])


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")