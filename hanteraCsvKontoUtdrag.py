import os
import csvhandler

def main():
    #year = input("Mata in år: ")
    year = "2024"
    #period = input("Mata in period 1 eller 2: ")
    period="1"
    #belopp = input("Mata in faktura belopp: ")
    belopp="6000"
    
    #filnamn = input("Mata in namn på csv kontoutdrag: ")   
    filnamn="test1.csv"

    while True:
        #Visa huvudmeny
        val = huvudmenu(belopp, period, year)

        if val == "1":
            
            csvhandler.print_csv_file_belopp(filnamn, belopp)
        elif val == "2":#Avsluta
            break

        elif val == "3":#Avsluta
            csvhandler.print_csv_file(filnamn)

        elif val == "9":#Avsluta
            break

        else:
            print("Ogiltig inmatning!")


def huvudmenu(belopp, period, year):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n------------------------------------------\n")
    print("\t-MENU- \U0001F603")
    print(f"\t1. Visa inbetalningar på {belopp}kr från csv kontoutdrag sorterat på datum")#order by datum
    print(f"\t2. Visa inbetalningar på {belopp}kr från csv kontoutdrag sorterat på husnr")#order by husnr
    print("\t3. Visa hela kontoutdraget")#order by datum
    print("\t4. Lista årets betalningar för valt år")#Order by husnr
    print("\t5. Föröver batalningar från csv kontoutdrag till DB")
    print("\t6. Lista betalningar från Db för valt år och period")
    print("\t7. Tabort faktura")
    print("\t8. Uppdatera faktura")
    print("\t9. Avsluta")
    
    val = input("\n\tMata in val: ")
    return val



main()