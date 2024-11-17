import duckdb
import pandas as pd

def print_csv_file(filename:str):
    
    try:
        sqlfraga =f'SELECT * FROM "{filename}" ORDER BY Transdag ASC LIMIT 100'
        content = duckdb.sql(sqlfraga).show(max_rows=200)        
        print(content) 


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
    
    sqlfraga1 = f'SELECT * FROM "{filename}" WHERE Belopp={belopp} ORDER BY Transdag ASC LIMIT 100'
    content = duckdb.sql(sqlfraga1).show(max_rows=200)        
    print(content) 
    klar=input("fortsätta? press enter")