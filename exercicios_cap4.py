#Exercício 1 — O Inspector de Texto
frase = input("Escreva a sua frase aqui, por favor: ")
print(frase.upper())
print(len(frase))
print(frase[::-1])
print(frase.lower().count("a"))

#Exercício 2 — Contador de Vogais
frase = input("Escreva a sua frase aqui, por favor: ")
contador = 0
for letras in frase:
    if letras.lower() in "aeiou":
        contador = contador + 1
print(f"O numero de vogais encontradas foram: {contador}")