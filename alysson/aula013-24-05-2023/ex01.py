"""#1-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido."""

print("="*50)
nota = float(input("Digite uma nota: "))
while nota < 0 or nota > 10:
        print(f'{nota} invalida')
        nota = float(input("Digite outra nota: "))

print(f"ok {nota} valida")

