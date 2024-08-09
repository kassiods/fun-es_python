def calcular_area(largura, comprimento, unidade="m²"):
    area=largura*comprimento
    print(f"A area é{area}{unidade}")
#chamadas da função
calcular_area(10,5) #usando valores padrao
calcular_area(largura=3, comprimento=4, unidade="cm²")#usando argumentos nomeados