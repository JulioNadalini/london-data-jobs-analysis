utilizador = {
    "nome": "Jujuba",
    "idade": "30",
    "email": "jujuba@email.com"
}

utilizador["cidade"] = "Londres"

utilizador["idade"] = "33"

print(f"O dicionario completa sera {utilizador}")

#Exercicio 2 - Acesso seguro (.get())
utilizador = {
    "nome": "Jujuba",
    "idade": 30,
}
chave_pesquisada = input("Digite o nome de uma chave: ")
print(utilizador.get(chave_pesquisada, "Chave nao encontrada"))

#Exercicio 3
turma = []

for i in range(2):
    print(f"CADASTRO DE ALUNO {i+1}")
    nome_digitado = input("Digite o nome do aluno: ")
    idade_digitada = int(input("Digite a idade do aluno: "))

    aluno = {"nome" : nome_digitado ,"idade": idade_digitada}

    turma.append(aluno)

print("LISTA COMPLETA")
print(turma)

#Exercicio 4
cores = ("vermelho", "verde", "cinza")
cores[0] = "rosa"

print(f"As cores encontradas sao:{cores}. A cor nova introduzida e {cores[0]}")
