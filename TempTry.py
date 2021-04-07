print("Programa que converte temperaturas")
print("Escolha o tipo de conversao")
print("----------------------------------------")
print("Codigo | Funcao")
print("  1    | Celsius para Fahrenheit")
print("  2    | Fahrenheit para Celsius")

ver=0

while(ver==0):
    try:
        codigo = int(input("codigo:"))

        if codigo == 1:
            C = float(input("Insira a temperatura em Celsius:"))
            F = (C * 9 / 5) + 32
            print(F, "Fahrenheit")
            ver=1

        elif codigo == 2:
            F = float(input("Insira a temperatura em Fahrenheit:"))
            C = (F - 32) * 5 / 9
            print(C, "Celsius")
            ver=1

        else:
            print("Valor invalido, digite novamente")
    except ValueError:
        print("Valor Invalido, digite novamente")