def minha_funcao(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}:{valor}")

minha_funcao(nome="Alice", idade="30", cidade="São Paulo")