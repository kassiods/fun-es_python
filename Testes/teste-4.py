#variavel global são definidas no nível superior do código Python, fora de qualquer função ou classe

y=20 #variavel global

def outra_funcao():
    print(y)

outra_funcao()
print(y)