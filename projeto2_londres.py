import pandas as pd

df = pd.read_csv('data_scientist.csv')

vagas_totais = len(df)
print(f"O numero total de vagas e: {vagas_totais}")

vagas_python = df[df['Description'].str.contains('python', case = False)]

print(f"O numero de vagas disponiveis para python sao: {len(vagas_python)}")

vagas_sql = df[df['Description'].str.contains('sql', case = False)]
print(f"O numero de vagas disponiveis para sql sao: {len(vagas_sql)}")

percentage_vagas_python = round(len(vagas_python) * 100/ vagas_totais, 1)
print(f"A porcentagem de vagas de python sao: {percentage_vagas_python}")

percentage_vagas_sql = round(len(vagas_sql) * 100/ vagas_totais, 1)
print(f"A porcentagem de vagas de sql sao: {percentage_vagas_sql}")

top_empresas = df['Company'].value_counts().head(3)
print ("TOP 3 EMPRESAS QUE MAIS CONTRATAM")
print(top_empresas)