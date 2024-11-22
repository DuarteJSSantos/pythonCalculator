#funcoes
def ask2numbers():
    while True:
        try:
            n1 = float(input("Introduza o primeiro numero: "))
            break
        except:
            print("Número invalido. Introduza um número real positivo ou negativo.")

    while True:
        try:
            n2 = float(input("Introduza o segundo numero: "))
            break
        except:
            print("Número invalido. Introduza um número real positivo ou negativo.")

    return [n1,n2]

def add():
    numbers = ask2numbers()
    print(f"Resultado: {numbers[0] + numbers[1]}\n")

def sub():
    numbers = ask2numbers()
    print(f"Resultado: {numbers[0] - numbers[1]}\n")

def mult():
    numbers = ask2numbers()
    print(f"Resultado: {numbers[0] * numbers[1]}\n")

def div():
    numbers = ask2numbers()
    print(f"Resultado: {numbers[0] / numbers[1]}\n")

def power():
    while True:
        try:
            base = float(input("Introduza a base da potencia: "))
            break
        except:
            print("Número invalido. Introduza um número real positivo ou negativo.")

    while True:
        try:
            exponent = float(input("Introduza o expoente: "))
            break
        except:
            print("Número invalido. Introduza um número real positivo ou negativo.")

    print(f"Resultado: {pow(base, exponent)}\n")

def root():
    while True:
        try:
            num = float(input("Introduza o numero (radicando): "))
            break
        except:
            print("Número invalido. Introduza um número real positivo ou negativo.")

    while True:
        try:
            radical = float(input("Introduza o radical: "))
            break
        except:
            print("Número invalido. Introduza um número real positivo ou negativo.")

    print(f"Resultado: {pow(num, 1/radical)}\n")

def showOperators():
    print("\nOperadores válidos:\nsoma-> +\nsubtracao-> -\nmultiplicacao-> x X *\ndivisao-> / :\npotencia-> ^ p P **\nraiz-> r R */\n")

#
# "main"
#
showOperators()
while True:

    print("Para ver os operadores introduza 'o' ou 'O'.\nPara sair introduza 's' ou 'S'")
    operator = input("Operacao a realizar: ")

    if operator in "oO":
        showOperators()
    elif operator in "sS":
        break
    elif operator in "+":
        add()
    elif operator in "-":
        sub()
    elif operator in "xX*":
        mult()
    elif operator in "/:":
        div()
    elif operator in "pP^**":
        power()
    elif operator in "rR*/":
        root()
    else:
        print("Operador inválido, tente novamente.\n")

    

