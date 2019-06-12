#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@ifc-araquari.edu.br>
# Lista de exercícios 5 - repetição com while


def quantidade_de_impares(valor_inicial, valor_final):
    ''' Determine a quantidade de números ímpares num intervalo'''

    impares = 0
    x = valor_inicial + 1

    while x < valor_final:
        if x % 2 == 1:
            impares += 1
        x += 1
    else:
        return impares

def soma_dos_inteiros(valor1, valor2):
    ''' Calcule a soma dos números inteiros no intervalo entre 'valor1'
    e o 'valor2' ou vice-versa, considerando que podem ser informado
    números negativos ou fora de ordem.
    Ex: 1 e 5 ou 5 e 1, retorna 9'''

    if valor1 < valor2:
        xi = valor1
        xf = valor2
    else:
        xi = valor2
        xf = valor1

    soma = 0
    xi += 1

    while xi < xf:
        soma += xi
        xi += 1

    return soma

def potencia(base, expoente):
    ''' Calcule a 'base' elevada ao 'expoente' manualmente sem usar
    'base**expoente'. Considere base e expoente como inteiros positivos.'''

    x = 1
    result = base
    if expoente != 0:
        while x < expoente:
            result *= base
            x += 1
    else:
        return 1

    return result

def crescimento_populacional(populacao1, populacao2, crescimento1,
                             crescimento2):
    ''' Calcule quantos anos levará para a 'população1' ultrapassar a
    'população2', baseado em suas porcentagens de crescimento.'''

    anos = 0
    crescimento1 /= 100
    crescimento2 /= 100

    if crescimento2 >= crescimento1:
        anos = 0
    else:
        while populacao1 < populacao2:
            populacao1 += (populacao1 * crescimento1)
            populacao2 += (populacao2 * crescimento2)
            anos += 1

    return anos

def Fibonacci(n):
    ''' Retorne o n-ésimo valor da série de Fibonacci
    Fibonacci = 1,1,2,3,5,8,13,...'''

    result = 0
    atual = 1
    count = 0

    while count < n:
        ant = atual
        atual = result
        result = atual + ant

        count += 1

    return result

def fatorial(numero):
    ''' Calcule e retorne o fatorial do 'numero' informado,
    O fatorial é o valor produtório dos valores menores ou iguais ao número
    ex: fatorial de 4 é 4*3*2*1 e retorna 24'''

    result = 1

    while numero > 0:
        result *= numero
        numero -= 1

    return result



def é_primo(valor):
    ''' Verifique se o 'valor' informado é primo.
    Um número primo é aquele que é divisível apenas por ele mesmo e por 1'''

    divisiveis = 0
    count = valor

    while count > 0:
        if valor % count == 0:
            divisiveis += 1

        count -= 1

    if divisiveis > 2 or valor == 0 or valor == 1:
        return False
    else:
        return True

def quantidade_de_primos(comeco, final):
    ''' Retorne a quantidade de primos entre os valores informados'''


    qnt_primos = 0

    while comeco < final:
        comeco += 1
        if é_primo(comeco):
            qnt_primos += 1

    return qnt_primos

def lista_de_primos(inicio, fim):
    '''Retorne uma lista de primos entre os valores informados, incluindo
    os limites'''

    numeros = []

    while inicio <= fim:
        if é_primo(inicio):
            numeros.append(inicio)

        inicio += 1
    return numeros

def serie1(n):
    '''Dado n, calcule o valor de
    s = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n '''

    count = 1
    s = 0

    while count <= n:
        s += (1/count)
        count += 1

    return round(s, 2)

def serie2(n):
    '''Dado n, calcule o valor de
    s = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m'''

    count = 1
    dividendo = 1
    divisor = 1
    res = 0

    while count <= n:
        res += dividendo/divisor
        dividendo += 1
        divisor += 2
        count += 1
    return round(res, 2)


def serie_pi(n):
    ''' Calcule o valor de pi através da série
    4/1 - 4/3 + 4/5 - 4/7 + ... - 4/m, sendo informado
    o número n de iterações '''

    count = 0
    divisor = 1
    res = 0

    while count < n:

        if count % 2 == 0:
            res += 4/divisor
        else:
            res -= 4/divisor

        count += 1
        divisor += 2

    return round(res, 6)

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31mFalhou'
    else:
        prefixo = '\033[32mPassou'
        acertos += 1
    print('{} Esperado: {} \tObtido: {}\033[1;m'.format(
        prefixo, esperado, obtido))


def main():
    print('Quantidade de ímpares:')
    test(quantidade_de_impares(1, 3), 0)
    test(quantidade_de_impares(1, 4), 1)
    test(quantidade_de_impares(1, 5), 1)
    test(quantidade_de_impares(1, 10), 4)
    test(quantidade_de_impares(1, 50), 24)
    test(quantidade_de_impares(1, 60), 29)
    test(quantidade_de_impares(40, 80), 20)

    print('Soma de números inteiros:')
    test(soma_dos_inteiros(1, 50), 1224)
    test(soma_dos_inteiros(50, 1), 1224)
    test(soma_dos_inteiros(10, 1), 44)
    test(soma_dos_inteiros(-10, 1), -45)
    test(soma_dos_inteiros(10, -10), 0)

    print('Potência:')
    test(potencia(2, 1), 2)
    test(potencia(2, 2), 4)
    test(potencia(1, 20000), 1)
    test(potencia(2, 4), 16)
    test(potencia(10000, 1), 10000)
    test(potencia(2, 10), 1024)
    test(potencia(2, 0), 1)
    test(potencia(10, 0), 1)

    print('Aumento da população:')
    test(crescimento_populacional(80000, 200000, 3, 1.5), 63)
    test(crescimento_populacional(1000, 2000, 1, 1.1), 0)
    test(crescimento_populacional(2000, 1000, 1.1, 1), 0)
    test(crescimento_populacional(2000, 2020, 1.1, 1), 11)

    print('Fibonnaci:')
    test(Fibonacci(1), 1)
    test(Fibonacci(2), 1)
    test(Fibonacci(3), 2)
    test(Fibonacci(4), 3)
    test(Fibonacci(5), 5)

    print('Fatorial:')
    test(fatorial(0), 1)
    test(fatorial(1), 1)
    test(fatorial(5), 120)
    test(fatorial(10), 3628800)

    print('Primo:')
    test(é_primo(0), False)
    test(é_primo(1), False)
    test(é_primo(2), True)
    test(é_primo(3), True)
    test(é_primo(4), False)
    test(é_primo(5), True)
    test(é_primo(7), True)
    test(é_primo(11), True)
    test(é_primo(121), False)
    test(é_primo(169), False)

    print('Quantidade de primos no intervalo:')
    test(quantidade_de_primos(5, 10), 1)
    test(quantidade_de_primos(10, 20), 4)
    test(quantidade_de_primos(0, 21), 8)
    test(quantidade_de_primos(43, 102), 12)

    print('Lista de primos:')
    test(lista_de_primos(0, 1), [])
    test(lista_de_primos(5, 10), [5, 7])
    test(lista_de_primos(10, 20), [11, 13, 17, 19])
    test(lista_de_primos(0, 21), [2, 3, 5, 7, 11, 13, 17, 19])
    test(lista_de_primos(43, 102), [43, 47, 53,
                                    59, 61, 67, 71, 73, 79, 83, 89, 97, 101])

    print('Série 1:')
    test(serie1(1), 1.00)
    test(serie1(15), 3.32)
    test(serie1(10), 2.93)
    test(serie1(5), 2.28)

    print('Série 2:')
    test(serie2(1), 1.00)
    test(serie2(2), 1.67)
    test(serie2(3), 2.27)
    test(serie2(4), 2.84)

    print('Série pi:')
    test(serie_pi(1), 4.000000)
    test(serie_pi(2), 2.666667)
    test(serie_pi(3), 3.466667)
    test(serie_pi(4), 2.895238)
    test(serie_pi(5), 3.339683)
    test(serie_pi(6), 2.976046)
    test(serie_pi(7), 3.283738)
    test(serie_pi(8), 3.017072)
    test(serie_pi(9), 3.252366)
    test(serie_pi(10), 3.041840)
    test(serie_pi(100), 3.131593)
    test(serie_pi(150), 3.134926)
    test(serie_pi(1000), 3.140593)
    test(serie_pi(5000), 3.141393)
    test(serie_pi(9000), 3.141482)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")