def abrevia_nome(nome_completo):
    '''Crie uma função que receba o nome completo de uma pessoa e devolva o primeiro e
    o último nomes, mais as iniciais do meio.
    Exemplo: EDSON ARANTES SOARES DO NASCIMENTO -> EDSON A S NASCIMENTO'''

    nome_cmplt = nome_completo.split()

    novo_nome = ''


    for nome in nome_cmplt:
        if nome == nome_cmplt[0] or nome == nome_cmplt[-1]:
            novo_nome += nome + ' '
        else:
            if len(nome) > 3:
                nome = nome[0]
                novo_nome += nome + ' '

    return novo_nome

print(abrevia_nome('EDSON ARANTES SOARES DO NASCIMENTO'))