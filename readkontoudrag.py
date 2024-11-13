import pandas as pd
import sqlite3

# Läs in CSV-filen
df = pd.read_csv('kontoutdrag.csv')

# Anslut till SQLite-databasen
conn = sqlite3.connect('hus.db')
cursor = conn.cursor()

# Sök efter specifika inbetalningar (exempelvis med ett visst belopp)
inbetalningar = df[df['Belopp'] == 1000]  # Anpassa till ditt sökkriterium

# Iterera över varje rad i resultatet
for index, row in inbetalningar.iterrows():
    referens = row['Referens']  # Ersätt med din kolumn för referens

    # Sök efter huset i databasen baserat på referensen
    cursor.execute("SELECT * FROM hus WHERE referens=?", (referens,))
    hus = cursor.fetchone()

    if hus:
        # Uppdatera hus-tabellen för att markera betalning
        hus_id = hus[0]  # Anta att första kolumnen är ID
        cursor.execute("UPDATE hus SET betalt=1 WHERE id=?", (hus_id,))
        print(f"Betalning från hus {hus_id} registrerad.")
    else:
        print(f"Hittade inget hus med referens {referens}")

# Commit changes and close connection
conn.commit()
conn.close()