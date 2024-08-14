'''
1-Crie um progama que calcule os 100mil primeiros numeros da sequencia de fibonacci
2-O progama deverá fazer isso através de uma função, com uma versão recursiva a outra não recursiva
3-O progama deverá verificar qual das versões da função efetua o calculo mais rápido.
'''

import random
import time

lista=[]
for i in range(100000):
    lista.append(random.randint (0,1000000))

