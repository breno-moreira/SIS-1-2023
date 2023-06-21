"""
E se o enunciado fosse "Faça um programa que soma X números gerados aleatoriamente no intervalo de 1 a 10, onde X é informado pelo usuário"?
"""
######## REPETIÇÂO CONTAVEL______posso utilizar o  a estrutura for
print('='*50)
import random
x = int(input("Digite a quantidade de números: "))
soma = 0
contador = 1
while contador <= x:
    sortedado = random.randint(1,10)
    print(f"Sorteado {sortedado}")
    soma = soma + sortedado
    contador = contador + 1
print(f"A soma foi de {soma}:")
print('='*50)