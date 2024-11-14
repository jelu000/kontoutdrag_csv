import os
import csvhandler

def main():
    year = input("Mata in år: ")
    period = input("Mata in period 1 eller 2: ")
    belopp = input("Mata in faktura belopp: ")
    filnamn = input("Mata in namn på csv kontoutdrag: ")   

    while True:
        #Visa huvudmeny
        val = huvudmenu()

        if val == "1":
            print("1")
            csvhandler.print_csv_file(filnamn)
        
        elif val == "9":#Avsluta
            break

        else:
            print("Ogiltig inmatning!")


def huvudmenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n------------------------------------------\n")
    print("\t-MENU- \U0001F603")
    print("\t1. Visa betalningar från csv kontoutdrag")#order by datum
    print("\t2. Föröver batalningar från csv kontoutdrag till DB")
    print("\t3. Lista betalningar från Db för valt år och period")#order by datum
    print("\t4. Lista årets betalningar för valt år")#Order by husnr
    print("\t5. Lista fakturor")
    print("\t6. Läggtill faktura")
    print("\t7. Tabort faktura")
    print("\t8. Uppdatera faktura")
    print("\t9. Avsluta")
    
    val = input("\n\tMata in val: ")
    return val



main()