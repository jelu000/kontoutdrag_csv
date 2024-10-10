import pandas as pd

#läser fil
df = pd.read_csv("Transaktioner_2024_jens_sept.csv", skiprows=1, encoding="windows-1252")
print(df.head()) 

totalt_belopp = df['Belopp'].sum()
print(f"Totalt belopp: {totalt_belopp}")