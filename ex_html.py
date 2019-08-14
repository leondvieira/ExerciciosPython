arquivo = open('home.html', 'a')

titulo = input('Digite o Titulo da Página:')
cabecalho = input('Digite o Cabecalho da Página:')

arquivo.write('''<HTML><head><title>{}</title></head><body><h1>{}</h1>'''.format(titulo, cabecalho))

resp = 's'

while resp == 's':
    nome_link = input('Nome do link:')
    link = input('Endereço do link:')
    texto = input('Texto da postagem:')

    arquivo.write('''<a href="https://{}">{}</a><p>{}</p>'''.format(link, nome_link, texto))

    resp = input('Você quer adicionar outro link? (s/n):')

arquivo.write('''</body></html>''')
