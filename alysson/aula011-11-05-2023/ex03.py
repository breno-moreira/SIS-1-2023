""""Programa que imprime a soma de todos os numeros PARES entre dois numerois quaisquer, incluindo-os 
Vamos assumir que num1< num2
    exemplo num1=10, num2=40
"""

print("="*50)
num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
soma = 0 

for i in range(num1,num2+1):
    #verificar se o i e par
    if i%2 == 0:
        print(i)
        soma = soma + 1 

print(f"A soma dos pares no intervalo[ {num1},{num2}] e {soma}")
print("="*50)