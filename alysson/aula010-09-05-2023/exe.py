"""Faça um progama que gere números inteiros aleatórios entre 1 e 10 e calcule a soma desses números, até que seja gerado um número num que foi informado pelo usuário anteriomente.
---Dica 1:antes de mais nada, peça para o usuário digitar um número de 1 a 10 e guardar o valor em num
---Dica 2:use a função randint(inicio, fim ) do módulo random para gerar um número aleatório entre 1 e 10"""
#importações de bibliotecas
import random #biblioteca util para trabalhar com valores aleatórios

#Inicializar a variavel soma
soma=0

print("-"*50)
num_sorte = int(input("Digite o número da sorte: "))
while num_sorte < 1 or num_sorte > 10:
    #quando num_sorte for invalido
    print("Número Inválido, digite um valor entre 1 e 10")
    num_sorte = int(input("Digite um número da sorte:"))
print("-"*50)

sorteado = random.randint(1,10)
while sorteado != num_sorte:
    soma = soma +sorteado
    sorteado = random.randint(1,10)

print(f"A soma final foi de {soma}")