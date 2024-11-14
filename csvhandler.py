import duckdb

def print_csv_file(filename:str):
    content=duckdb.read_csv(filename)
    print(content)
    klar=input("Nöjd?")