def adicao (a,b):
    return a+b
def subtracao (a,b):
    return a-b
def multiplicacao (a,b):
    return a*b
def divisao (a,b):
    if b==0:
        print("Não é possivel dividir por zero")
    else:
        return a/b
      
def menu():
    print("Escolha a operação:")
    print("1-Adição")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão")
    print("5-Sair")

while(True):
    menu()
    opcao="0"
    opcao=int(input("opção: "))
    a=int(input("Digite o primeiro numero: "))
    b=int(input("Digite o segundo numero: "))
    if opcao==1:
        print("resultado igual a = ", adicao(a,b))
    elif opcao==2:
        print("resultado igual a = ", subtracao(a,b))
    elif opcao==3:
        print("resultado igual a = ", multiplicacao(a,b))
    elif opcao==4:
        print("resultado igual a = ", divisao(a,b))
    elif opcao==5:
        break
    else:
        print("opção invalida.")
