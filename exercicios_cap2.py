
# Exercicio 1
print("Ola, esta e uma calculadora simples!")
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
operacao = input("Digite a operacao desejada (+, -, *, /): ")

if operacao == "+":
    num3 = num1+num2

    print(f"O resultado da soma entre {num1} e {num2} e: {num3}")

elif operacao == "-":
    num3 = num1-num2

    print(f"O resultado da subtracao entre {num1} e {num2} e: {num3}")

elif operacao == "*":
    num3 = num1*num2
    print(f"O resultado da multiplicacao entre {num1} e {num2} e: {num3}")

elif operacao == "/":
    if num2 == 0:
        print("Nao e possivel dividir por zero!")
    else:
        num3 = num1/num2
        print(f"O resultado da divisao entre {num1} e {num2} e: {num3}")   

#Exercicio 2
print("Este e um programa que a area de um circulo!")
raio = float(input("Digite o raio do circulo: "))
area = 3.14 * (raio ** 2)
print(f"O tamanho da area do circulo e {area}")

#Exercicio 3
print("Conversor de temperatura de Celsius para Fahrenheit")
conversor = float(input("Digite a temperatura em Celsius: "))
convertendo = conversor * 9/5 + 32
print(f"A conversao do valor {conversor} em Celsius para Fahrenheit e: {convertendo}")
