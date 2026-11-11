"""Exercício 1 — O ciclo for simples
Escreve um ciclo for que imprima os números de 1 a 10 no ecrã.
(Dica: usa range(1, 11) porque o 11 fica de fora).

Exercício 2 — O continue (O saltador)
Escreve um ciclo for que vá de 1 a 20. No entanto, se o número for múltiplo de 3 (ou seja, se numero % 3 == 0), o ciclo deve usar o continue para saltar esse número e não o imprimir.
(O operador % dá-te o resto da divisão. Se o resto for 0, é múltiplo).

Exercício 3 — A Password (Ciclo while)
Pede ao utilizador para digitar a password (a password correta é "python123"). Enquanto o utilizador errar, o programa deve dizer "Password incorreta, tente novamente". Quando ele acertar, o ciclo termina e o programa imprime "Acesso concedido!".
(Dica: cria uma variável password = "" antes do ciclo para ele poder começar).

Exercício 4 — A Tabuada
Pede um número ao utilizador (com int(input(...))). Depois, usa um ciclo for para imprimir a tabuada desse número de 1 a 10. Exemplo de saída: 5 x 1 = 5, 5 x 2 = 10, etc.
(Dica: podes usar f-strings dentro do print para juntar o número, o "x" e o resultado).

Exercício 5 — Soma de 5 números
Pede 5 números ao utilizador (podes usar um ciclo for que corre 5 vezes). No final, imprime a soma de todos os números que ele digitou.
(Dica: cria uma variável soma = 0 antes do ciclo, e dentro do ciclo faz soma = soma + numero)."""

"""Exercício 1 — O ciclo for simples"""
for i in range(1, 11):
    print(f"os numeros encontrados sao {i}")

"""Exercício 2 — O continue (O saltador)"""
for i in range(1,21):
    if i % 3 == 0:
        continue
    print(i)

#Exercício 3 — A Password (Ciclo while)
print("Para fazer o login")
password = ""

while password != "python123":
    password = input("Insira a sua password: ")
    
    
    if password != "python123":
        print("Password incorreta, tente novamente.")

print("Acesso concedido!")

#PIN do cartao
print("Estamos acessando a sua conta bancaria!")
pin = ""
while pin != "1234":
    pin = input("Insira o seu pin")

    if pin != "1234":
        print("PIN nao aceito, tente novamente!")

print("PIN aceito!")

#MENU DE OPCOES
print("Menu de opcoes do restaurante")
print("1 - Pizza")
print("2 - Hamburger")
print("0 - Sair")
opcao = ""

while opcao != "0":
    opcao = input("Insira a sua opcao:")
    
    if opcao == "1":
        print(f"Voce escolheu a opcao:{opcao} Pizza!")
    elif opcao == "2":
        print(f"Voce escolheu a opcao:{opcao} Hamburger!")
    elif opcao == "0":
         print(f"Obrigado por escolher o nosso resturante")
    else:
        print("Opcao invalida! Tente Novamente")
print("Programa encerrado.")
    
#Adivinhar o numero secreto
secreto = 42
palpite = 0

while palpite != secreto:
    palpite = int(input("Forneca o numero secreto: "))

    if palpite > secreto:
        print("Muito alto! Tente um número menor.")
    elif palpite < secreto:
        print("Muito baixo! Tente um número maior.")

print(f"Parabéns, acertaste!")

#Acumulador com "Sair"
soma = 0
numero = ""

while numero != "sair":
    numero = input("Digite um número ou 'sair': ")
    
    if numero == "sair":
        print("A encerrar o programa...")
    else:
        numero_inteiro = int(numero)
        soma = soma + numero_inteiro
        print(f"Soma atual: {soma}")
print(f"A soma total foi: {soma}")


#Caixa eletronico
saldo = 0
meta = 1000
deposito= ""

while saldo < meta:
    deposito = int(input("Insira o valor em numeros a ser depositado: "))
    saldo = saldo + deposito
    print(f"Saldo atual: {saldo}")
print("Parabens! Ja podes comprar o computador!")


#Exercício 4 — A Tabuada
