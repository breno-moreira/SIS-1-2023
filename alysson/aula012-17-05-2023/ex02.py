""" faca um programa para determinar o numero de digitos de um numero inteiro positivo informado
EX: 
entrada: 20342 | saida: tem 5 digitos.
entrada: 2034  | saida: tem 4 digitos.
entrada: -3524 | saida: numero invalido.
"""
Numero = int(input("Digite um numero: "))
if Numero > 0:
    qtd = 0
    while Numero > 0:
        Numero = Numero // 10
        qtd += 1
    print(f"tem {qtd} Digitos:")
else:
    print ("numero invalido")
