#Exercicio 1
def boas_vindas(nome):
    print(f"Bem-vindo(a), {nome}!")

boas_vindas("Maria")
boas_vindas("Carlos")
boas_vindas("Paulo")

#Exercicio 2

def calcular(num1,num2,operacao):
    if operacao == "+":
        return num1+num2
    elif operacao == "-":
        return num1-num2
    elif operacao == "*":
        return num1*num2
    elif operacao == "/":
        if num2 ==0:
            return "Essa divisao e impossivel de ser efetuada!"
        else:
            return num1/num2
    else:
        return "Operacao invalida!"

print(calcular(10, 5, "+")) 
print(calcular(10, 5, "-"))  
print(calcular(10, 5, "*")) 
print(calcular(10, 5, "/")) 
print(calcular(10, 0, "/"))
print(calcular(0, 10, "/"))

#Exercicio 3 - verificador de par ou impar
def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

if e_par(61):
    print("O número é par!")
else:
    print("O número é impar!")

#Exercicio 4
def maior_de_tres(a,b,c):
    if a > b and a > c:
        return f"O maior numero sera: {a}"
    elif b > a and b > c:
        return f"O maior numero sera {b}"
    else:
        return f"O maior numero sera {c}"

print(maior_de_tres(20, 5, 2)) # 10
print(maior_de_tres(15, 10, 2)) # 10
print(maior_de_tres(5, 2, 10)) # 10