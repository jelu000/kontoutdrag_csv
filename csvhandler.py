import duckdb
import pandas as pd

def print_csv_file(filename:str):
    
    try:
        #sqlfraga =f'SELECT * FROM "{filename}" ORDER BY Bokföringsdag ASC LIMIT 100'
        sqlfraga =f'SELECT * FROM "{filename}" ORDER BY Transdag ASC LIMIT 100'
        content = duckdb.sql(sqlfraga).show(max_rows=200)        
        print(content) 

        print("Pandas")

        pd.set_option('display.max_rows', None)  # Visa alla rader
        pd.set_option('display.max_columns', None)  # Visa alla kolumner
        pd.set_option('display.width', None)  # Anpassa bredden för utskriften
        df = pd.read_csv(filename)
        # Sök efter specifika inbetalningar (exempelvis med ett visst belopp)
        #inbetalningar = df[df['Belopp'] == belopp]  # Anpassa till ditt sökkriterium

        print(df)


        #con = duckdb.connect()
        # Visa alla rader
        #con.execute("SET show_max_rows = 0")

        # Läs in CSV-filen och visa resultatet
        #content = con.execute(sqlfraga2).fetchall()
        #print(content)

        #df = pd.read_csv(filename, engine="python", on_bad_lines='skip', skiprows=1, nrows=200, encoding="utf-8")
        #print(df.head())
    except UnicodeError:
        print("utf-8 fungerade inte, testar latin1...")
        #df = pd.read_csv("konto_historik.csv", encoding="latin1")

    klar=input("fortsätta? press enter")

def print_csv_file_belopp(filename, belopp):
    
    #sqlfraga1 = f'SELECT * FROM "{filename}" WHERE Belopp={belopp} ORDER BY Bokföringsdag ASC LIMIT 100'
    sqlfraga1 = f'SELECT * FROM "{filename}" WHERE Belopp={belopp} ORDER BY Transdag ASC LIMIT 100'
    #sql_antalrader = f'SELECT COUNT * FROM "{filename}" WHERE Belopp={belopp} ORDER BY Transdag ASC LIMIT 100'
    
    #antalrader = duckdb.sql(sql_antalrader).show(max_rows=200) 
    content = duckdb.sql(sqlfraga1).show(max_rows=200)        
    print(f"Hittade {type(content)} inbetalningar på {belopp}kr")
    print(content) 
    print("Pandas")

    
    
    pd.set_option('display.max_rows', None)  # Visa alla rader
    pd.set_option('display.max_columns', None)  # Visa alla kolumner
    pd.set_option('display.width', None)  # Anpassa bredden för utskriften
    #df = pd.read_csv(filename)
    
    
    # Läs in CSV-filen och specificera att den första raden innehåller kolumnrubriker
    df = pd.read_csv(filename, skiprows=1)  #0 betyder att den första raden är rubriker
    
    
    # Sök efter specifika inbetalningar (exempelvis med ett visst belopp)
    filter_df = df[df['Belopp'] == 6000]

    print(len(filter_df))
    #Visa de filtrerade raderna
    print(filter_df)
    #print(df.columns)
    #print(df)

    klar=input("fortsätta? press enter")