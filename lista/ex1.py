def conta_palavras(texto):
    '''
    Leia uma string com um texto completo e devolva um dicionário contendo as palavras
    e sua frequência
    '''


    palavras = (texto.lower()).split()
    dicionario = {}

    for palavra in palavras:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

    return dicionario


print(conta_palavras("Um carro vermelho vermelho legal!"))