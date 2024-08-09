def calcular_media(*numeros):
    return sum(numeros) / len(numeros)

#chamada da função
notas = [8,7,4,3]
media = calcular_media(*notas) #desempacotando a lista
print(f"a media é {media}")