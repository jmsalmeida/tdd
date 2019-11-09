'''
Imprimir uma escadinha com o caractere escolhidos e a quantidade de degraus
'''

def monta_escadinha(caractere, quantidade_degraus):
    escadinha = ''

    for i in range(0, quantidade_degraus):
        escadinha += caractere
        print(escadinha)

    return


caractere = input('Caractere: ')
quantidade_degraus = int(input('Degraus: '))

monta_escadinha(caractere, quantidade_degraus)
