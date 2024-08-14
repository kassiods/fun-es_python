def busca_binaria (lista, elemento,inicio,fim):
    if inicio>fim:
        return False
    meio = (inicio+fim) // 2
    if lista [meio]==elemento:
        return True
    elif lista[meio]>elemento:
        return busca_binaria(lista, elemento, inicio, meio-1)
    else:
        return busca_binaria(lista, elemento, inicio, meio+1)