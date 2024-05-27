selecao = 0

def somar():
    print("Somando numeros\n")
    num1 = 0
    num2 = 0

    num2 = int(input("Digite o segundo numero: "))
    num1 = int(input("Digite o primeiro numero: "))
    print(f"{num1} + {num2} é igual a {num1+num2}")

def subtrair():
    print("Subtraindo numeros\n")
    num1 = 0
    num2 = 0

    num2 = int(input("Digite o segundo numero: "))
    num1 = int(input("Digite o primeiro numero: "))
    print(f"{num1} - {num2} é igual a {num1-num2}")

def multiplicar():
    print("Multiplicando numeros\n")
    num1 = 0
    num2 = 0

    num2 = int(input("Digite o segundo numero: "))
    num1 = int(input("Digite o primeiro numero: "))
    print(f"{num1} * {num2} é igual a {num1*num2}")

def dividir():
    print("Somando numeros\n")
    num1 = 0
    num2 = 0

    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    print(f"{num1} / {num2} é igual a {num1/num2}")


while True:
    selecao = int(input("O que deseja?\n0 - Sair\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n"))
    match selecao:
        case 0:
            print("Encerrando...")
            quit()
        case 1:
            somar()
        case 2:
            subtrair()
        case 3:
            multiplicar()
        case 4:
            dividir()
        case _:
            print("[ERRO] Opção inválida, tente novamente! [ERRO]")
        