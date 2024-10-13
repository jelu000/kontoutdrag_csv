import os
import hus
from prettytable import PrettyTable
# pip install prettytable
#https://www.javatpoint.com/prettytable-in-python

#printMenu()-skriver ut muny
def printMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n------------------------------------------\n")
    print("\t-MENU- \U0001F603")
    print("\t1. Lista hus")
    print("\t2. Läggtill hus")
    print("\t3. Tabort hus")
    print("\t4. Avsluta")
    
    val = input("\n\tMata in val: ")
    return val

#createMotorcykle()-läser in ny Motorcykel och returnerar den
#return Motorcykel
def createHus():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n------------------------------------------")
    husnr = input("\n\tMata in husnummer: ")
    fnamn = input("\n\tMata in förnamn: ")
    enamn = input("\n\tMata in efternamn: ")
    epost = input("\n\tMata in epost adress: ")
    tel = input("\n\tMata in tel nr: ")
    #topphastighet = int(input("\n\tMata in topphastighet: "))

    return   hus.Hus(husnr, fnamn, enamn, epost, tel)
#List all motorcykles
def printListMotorcykel(lista_hus):
    os.system('cls' if os.name == 'nt' else 'clear')
    t_table = PrettyTable(['HusNr', 'Förnamn', 'Efternamn', 'Epost adress', 'Telefonummer', 'Id'])

    for huset in lista_hus:
        t_table.add_row([ huset.husnr, huset.fnamn, huset.enamn, huset.epost, huset.tel, huset.id])
    
    print(t_table)
    input("Fortsätta? tryck Enter: ")


def printDeleteMotorcykel():
    os.system('cls' if os.name == 'nt' else 'clear')
    return input("\tMata in id på motorcykel som ska tas bort: ")
    