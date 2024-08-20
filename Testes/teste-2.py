def calcular_media(numeros):
    soma=sum(numeros)
    quantidade=len(numeros)
    media = soma/quantidade
    return media

notas = []

notas.append(float(input("Digite a nota 1 do aluno: ")))
notas.append(float(input("Digite a nota 2 do aluno: ")))
notas.append(float(input("Digite a nota 3 do aluno: ")))
notas.append(float(input("Digite a nota 4 do aluno: ")))

media_final=calcular_media(notas)

print(f"A media é {media_final}")