def data_extenso(data):

    meses = {
         '01': 'janeiro',
         '02': 'fevereiro',
         '03': 'março',
         '04': 'abril',
         '05': 'maio',
         '06': 'junho',
         '07': 'julho',
         '08': 'agosto',
         '09': 'setembro',
         '10': 'outubro',
         '11': 'novembro',
         '12': 'dezembro',
    }

    dia = data[0:2]
    mes = data[3:5]
    ano = data[6::]

    return '{} de {} de {}'.format(dia, meses[mes], ano)

print(data_extenso('29/07/2019'))
