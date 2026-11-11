import pandas as pd

# Load the file we just copied
df = pd.read_csv("data_scientist.csv")

# Show the first 5 rows
print("--- First 5 rows ---")
print(df.head())

print(len(df))
print(df.shape)

print(df['Company'].head(10))

vagasmanager = df[df['Title'].str.contains('Manager')]
print(f"Total de vagas de Manager: {len(vagasmanager)}")
print(vagasmanager.head())

vagas_londres = df[df['Description'].str.contains('London')]
print(vagas_londres)

print(f"\nTotal de vagas que mencionam Londres: {len(vagas_londres)}")

print(vagas_londres[['Title', 'Company']].head())

vagas_skills = df[df['Description'].str.contains('python')]
print(vagas_skills.head(10))