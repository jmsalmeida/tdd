def filtrar_nomes(lista):
    lista_filtrada = []
    letra = input('Entre com a letra que deseja filtrar: ').upper()

    for item in lista:
        if item[0] == letra:
            lista_filtrada.append(item)

    if len(lista_filtrada) == 0:
        return 'Nenhum nome com a letra {} foi encontrado'.format(letra)
    else:
        return lista_filtrada

lista_alunos = [
    'Amanda Reges',
    'Amyr Mauricio',
    'Barbara Santos',
    'Beatriz Dias',
    'Caio Moreira',
    'Catharina Moral',
    'Edson Consegue',
    'Eduardo Henrique',
    'Felipe Honorio',
    'Fabio Santana',
    'Gabriel Miguel',
    'Gabrielle Lima',
    'Hevellin Alencar',
    'Hugo Erico',
]

print(filtrar_nomes(lista_alunos))



