def minha_funcao(*arg, **kwargs):
    print("Argumentos posicionais:", arg)
    print("Argumentos nomeados:", kwargs)

minha_funcao(1,2,3, nome="joao pedro", idade=17)