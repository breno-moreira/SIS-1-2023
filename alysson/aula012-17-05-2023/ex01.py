""" faca um programa para montar a tabela de multiplicação de numeros  de 1 a 10 (ex. 1x1 = 1, 1 x 2 = 2, etc) """

for contador in range(1,11):
    print("="*20)
    print(f"tabuada do {contador}")
    for fator in range(1,11):
        resultado = contador*fator 
        print(f"{contador} x {fator} = {resultado}")