"""2- Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações."""

print("-"*50)

Usuario = input("Digite seu nome: ")
senha = input("Digite sua senha: ")

while Usuario == senha:
    print("usuario e senha ao identicos, digite novamente")
    Usuario = input("Digite seu nome: ")
    senha = input("Digite sua senha diferente do usuario: ")

print("ok, usuario e semha valida")
print("="*50)