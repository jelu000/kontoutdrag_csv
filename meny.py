import os
import hus
import faktura
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
    print("\t4. Uppdatera hus")
    print("\t5. Lista fakturor")
    print("\t6. Läggtill faktura")
    print("\t7. Tabort faktura")
    print("\t8. Uppdatera faktura")
    print("\t9. Avsluta")
    
    val = input("\n\tMata in val: ")
    return val



#----------------------------------------------------------------------------------------------
#createHus()-läser in ny Hus och returnerar den
#return Hus
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

#createFaktura()-läser in ny Faktura och returnerar den
#return Faktura
def createFaktura():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n------------------------------------------")
    fakturanr = input("\n\tMata in fakturanr: ")
    year = int(input("\n\tMata år: "))
    husnr = input("\n\tMata in husnr: ")
    belopp = int(input("\n\tMata in belopp: "))
    betalningsstatus = int(input("\n\tMata in betalningsstaus 1-0: "))
    betalningsdatum = input("\n\tMata in betalningsdatum: ")
    f_id = input("\n\tMata in faktura id (year+fakturaNr+husNr): ")
    return   faktura.Faktura(fakturanr, year, husnr, belopp, betalningsstatus, betalningsdatum, f_id)

#-----------------------------------------------------------------------------------------------------


#List all hus
def print_list_hus(lista_hus):
    os.system('cls' if os.name == 'nt' else 'clear')
    t_table = PrettyTable(['HusNr', 'Förnamn', 'Efternamn', 'Epost adress', 'Telefonummer', 'Id'])

    for huset in lista_hus:
        t_table.add_row([ huset.husnr, huset.fnamn, huset.enamn, huset.epost, huset.tel, huset.id])
    
    print(t_table)
    input("Fortsätta? tryck Enter: ")


#List all fakturor
def print_list_fakura(lista_fakturor):
    os.system('cls' if os.name == 'nt' else 'clear')
    t_table_fakturor = PrettyTable(['FakturaNr', 'År', 'HusNr', 'Belopp', 'Betalningsstatus', 'Betalningsdatum', 'Faktura id', 'Id'])

    for faktura in lista_fakturor:
        t_table_fakturor.add_row([ faktura.fakturanr, faktura.year, faktura.husnr, faktura.belopp, faktura.betalningsstatus, faktura.betalningsdatum, faktura.f_id, faktura.id])
    
    print(t_table_fakturor)
    input("Fortsätta? tryck Enter: ")

#----------------------------------------------------------------------------------------------------------------------------------------


def printDeleteHus():
    os.system('cls' if os.name == 'nt' else 'clear')
    return input("\tMata in hus nr på hus som ska tas bort: ")

def printDeleteFaktura():
    os.system('cls' if os.name == 'nt' else 'clear')
    return input("\tMata in faktura nr på hus som ska tas bort: ")
