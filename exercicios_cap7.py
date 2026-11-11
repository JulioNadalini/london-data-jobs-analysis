#Exercicio 1
import random

frase = input("Escreva uma frase informando o que foi feito hoje no trabalho: ")

with open("diario.txt", "w") as ficheiro:
    ficheiro.write(frase)

print("Frase guardada com sucesso no diario.txt!")

#Exercicio 2 - leitor

with open("diario.txt", "r") as ficheiro:
    conteudo = ficheiro.read()
    print(conteudo)

#Exercicio 3 - input blindado
try:
    idade_digitada = int(input("Favor digite a sua idade: "))
    print(f"Idade registrada: {idade_digitada}")
except ValueError:
    print("Erro: isso nao e um numero valido!")

#Exercicio 4
numero_sorteado = random.randint(1,10)
numero_digitado = 0

while numero_digitado != numero_sorteado:
    try:
        numero_digitado = int(input("Tente adivinhar o numero sorteado, entre 1 e 10: "))
        if numero_digitado != numero_sorteado:
           print("Tente novamente!")
    except ValueError:
        print("Erro: isso nao e um numero valido")
print(f"Parabens! Voce achou o numero correto: {numero_sorteado}")