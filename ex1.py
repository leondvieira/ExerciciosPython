arquivo = open('numeros.txt', 'r')

# escrita

# for linha in range(1, 101):
#     arquivo.write('%d\n' % linha)

# leitura

# for linha in arquivo.readlines():
#     print(linha)

# leitura pythonic
with arquivo as f:
    print(f.read())

arquivo.close()
