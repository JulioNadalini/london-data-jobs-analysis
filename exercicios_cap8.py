import pandas as pd

dados = {
    "nome": ["Ana", "Rui", "Marta", "João"],
    "idade": [30, 25, 35, 28],
    "cidade": ["Londres", "Londres", "Porto", "Londres"]
}

df = pd.DataFrame(dados)

print(df)


dados2 = {
    "cargo": ["Gerente", "CEO", "CFO"],
    "salario": [1000, 4000, 5000],
    "cidade": ["Londres", "Londres", "Barcelona"]
}
df2 = pd.DataFrame(dados2)
print(df2)

londres = df2[df2["cidade"] == "Londres"]
print(londres)

mediasalarial = londres["salario"].mean()
print(f"A media salarial e de: {mediasalarial}")