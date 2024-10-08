'''
1-Crie um progama que calcule os 100mil primeiros numeros da sequencia de fibonacci
2-O progama deverá fazer isso através de uma função, com uma versão recursiva a outra não recursiva
3-O progama deverá verificar qual das versões da função efetua o calculo mais rápido.
'''

import time

#Função iterativa para calcular o n-ésimo número de Fibonacci
def fibonacci_iterativa(n):
    a, b = 1, 1
    for _ in range(2,n): #variando de 2 ate o numero que vai calcular
        a, b = b, a + b #vai pegar e retornar a e calcular os outros elementos
    return a

#Função recursiva para calcular o n-ésimo número de Fibonacci
def fibonacci_recursiva(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci_recursiva(n - 1) + fibonacci_recursiva(n - 2)


#Calculando e medindo o tempo da função iterativa
começa = time.time()
fibonacci_iterativa(10000)
tempo_interativo = time.time() - começa

# Calculando e medindo o tempo da função recursiva (com um número pequeno)
começa = time.time()
fibonacci_recursiva(10000)
tempo_recursivo = time.time() - começa

print(f"Tempo de execução da função iterativa: {tempo_interativo:.6f} segundos")
print(f"Tempo de execução da função recursiva: {tempo_recursivo:.6f} segundos")

# Comparando qual foi mais rápida
if tempo_interativo < tempo_recursivo:
    print("A função iterativa foi mais rápida.")
else:
    print("A função recursiva foi mais rápida.")