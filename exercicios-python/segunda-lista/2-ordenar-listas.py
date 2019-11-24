def escolher_ordem():
    print('Ordenar lista')
    print('1 - Ordem crescente')
    print('2 - Ordem decrescente')
    print('---------------------')
    print('')

    opcao = input('Escolha a ordem: ')
    return opcao

def ordenar_lista(lista):
    ordem = escolher_ordem()

    if ordem == '1':
        lista.sort()
        return(lista)
    elif ordem == '2':
        lista.sort(reverse=True)
        return lista
    else:
        return 'Opção não existe'


lista = [9, 6, 3, 5, 8, 1, 0, 4, 7, 2]

nova_lista = ordenar_lista(lista)

print(nova_lista)
