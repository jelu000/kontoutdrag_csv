#https://antares-sql.app/downloads
#https://pynative.com/python-sqlite/#h-create-sqlite-table-from-python
#https://www.sqlite.org/autoinc.html
#https://pynative.com/python-sqlite/

import sqlite3
from sqlite3 import Error

import hus
import faktura

class DbHandler:

    def __init__(self):
        

        self.db_name = "hus.db"
        t_hus = hus.Hus("145")
        
        print(f"hus DbHandler: {t_hus.get_hus().husnr}")
        
        self.create_conn_sqllite(self.db_name)
        self.create_table_hus()
        self.create_table_fakturor()
        

#------------------------------------------------------------------------------------------------------------
    def add_hus(self, t_hus: hus.Hus):
      
        sqliteConnection = sqlite3.connect(self.db_name)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = f"""INSERT INTO hus
                          (husnr, fnamn, enamn, epost, tel)  
                          VALUES  
                          ('{t_hus.husnr}', '{t_hus.fnamn}', '{t_hus.enamn}', '{t_hus.epost}', '{t_hus.tel}') """
        

        #print(sqlite_insert_query)
        #input("Vänta")
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print(f"Record HUS inserted successfully into SqliteDb_developers table {count} ", cursor.rowcount)
        cursor.close()


    def add_faktura(self, t_faktura: faktura.Faktura):
      
        sqliteConnection = sqlite3.connect(self.db_name)
        cursor = sqliteConnection.cursor()
        sqlite_insert_query = f"""INSERT INTO fakturor
                          (fakturanr, year, husnr, belopp, betalningsstatus, betalningsdatum, f_id)  
                          VALUES  
                          ('{t_faktura.fakturanr}', {t_faktura.year},'{t_faktura.husnr}', {t_faktura.belopp}, {t_faktura.betalningsstatus}, '{t_faktura.betalningsdatum}', '{t_faktura.f_id}') """
        

        #print(sqlite_insert_query)
        #input("Vänta")
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        print(f"Record Faktura inserted successfully into SqliteDb_developers table {count} ", cursor.rowcount)
        cursor.close()
            
#----------------------------------------------------------------------------------------------------------

    def deleteHus(self, t_husnr):
        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            cursor = sqliteConnection.cursor()
        

            # Deleting single record now
            sql_delete_query = f"""DELETE from hus where husnr = {t_husnr}"""
            cursor.execute(sql_delete_query)
            sqliteConnection.commit()
            print(f"\tMotorcykel med id {t_husnr} bortagen! ")
            cursor.close()

        except sqlite3.Error as error:
            print("\tFailed to delete record from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                #print("the sqlite connection is closed")  
#----------------------------------------------------------------------------------------
    def create_conn_sqllite(self, db_file):
        # create a database connection to a SQLite database
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()

        return conn
#----------------------------------------------------------------------------------------    

    def read_table_hus(self):

        lista_hus = []

        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            cursor = sqliteConnection.cursor()
            #print("Connected to SQLite")

            sqlite_select_query = """SELECT * from hus ORDER BY husnr"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Antal rader:  ", len(records), "\n")
            #print("Printing each row")
            
            '''for row in records:
                print("Id: ", row[0])
                print("Fabrikat: ", row[1])
                print("Modell: ", row[2])
                print("Kubik: ", row[3])
                print("Vikt: ", row[4])
                print("Hk: ", row[5])
                print("ToppHastighet: ", row[6])
                print("\n")
            '''   

            for row in records:
                t_hus = hus.Hus(row[1], row[2], row[3], row[4], row[5], row[0])
                lista_hus.append(t_hus)
                
                cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return lista_hus
    
    def read_table_faktura(self):

        lista_faktura = []

        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            cursor = sqliteConnection.cursor()
            #print("Connected to SQLite")

            sqlite_select_query = """SELECT * from fakturor ORDER BY husnr"""
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()
            print("Antal rader:  ", len(records), "\n")
            #print("Printing each row")
            
          

            for row in records:
                t_faktura = faktura.Faktura(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])
                lista_faktura.append(t_faktura)
                
                cursor.close()

        except sqlite3.Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")

        return lista_faktura

#----------------------------------------------------------------------------------------------------    
    #Skapar tabellen hus i databasen, körs bara första gången
    def create_table_hus(self):
        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS hus (
                                id INTEGER PRIMARY KEY,
                                husnr TEXT NOT NULL,
                                fnamn TEXT,
                                enamn TEXT,
                                epost TEXT,
                                tel TEXT);'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")



    #Skapar tabellen fakturor i databasen, körs bara första gången
    def create_table_fakturor(self):
        try:
            sqliteConnection = sqlite3.connect(self.db_name)
            sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS fakturor (
                                id INTEGER PRIMARY KEY,
                                fakturanr TEXT,
                                year INTEGER,
                                husnr TEXT,
                                belopp INTEGER,
                                betalningsstatus INTEGER,
                                betalningsdatum TEXT,
                                f_id TEXT);'''

            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            print("SQLite table created")

            cursor.close()

        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("sqlite connection is closed")