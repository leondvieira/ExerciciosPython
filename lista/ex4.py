'''
A Selma tem uma caderneta com as anotações de compras na cantina. Ela quer que você faça um programa
    que leia essas informações e grave um ARQUIVO NOVO de nome “totais.txt” com os nomes dos alunos e o
    valor total da dívida de cada um. A lista de entrada está em um arquivo texto de nome “entrada.txt”, no
    seguinte formato:
    Anita;3.5
    Beto;4.5
    Júlia;6.5
    Anita;4.0
    Anita;3.6
    Juarez;7.8
    Júlia;8.5
    A solução deve ser feita de forma modularizada, cada função cumprindo um objetivo. Carregue os dados do
    arquivo texto “entrada.txt” em um dicionário, fazendo a soma. Crie um arquivo novo de nome “totais.txt”, e insira
    os dados nele.
    Resultado no arquivo novo de nome “totais.txt” no formato:
    Aluno; total devido
'''

def soma_valores(nome, valor, dict):

    if nome in dict:
        dict[nome] += valor
    else:
        dict[nome] = valor
    return dict

def escreve_total(dict):
    arquivo = open('totais.txt', 'a')

    for chave in dict:
        arquivo.write('{};{}\n'.format(chave, dict[chave]))
    arquivo.close()

    return arquivo


def pega_informacoes(arquivo):
    arq = open(arquivo, 'r')
    dict = {}

    for line in arq:
        info = line.replace('\n', '').split(';')
        nome = info[0]
        valor = float(info[1])

        dict = soma_valores(nome, valor, dict)

    escreve_total(dict)
