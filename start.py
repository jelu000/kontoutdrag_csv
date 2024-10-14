import pandas as pd

import dbhandler
import meny



#läser fil
df = pd.read_csv("Transaktioner_2024_jens_sept.csv", skiprows=1, encoding="windows-1252")
#print(df.head()) 
#print(df)
#print(df['Referens'])



def main():
    
    
    #skapar datbas med klassen dbhandler
    db_handler = dbhandler.DbHandler()


    while True:
        val = meny.printMenu()

        if val == "1":#Lista Hus

            #print("Val 1")
            #input("\tFortsätta? tryck Enter: ")
            lista_hus = db_handler.read_table_hus()
            mc = meny.print_list_hus(lista_hus)
            
                        
        elif val == "2":#lägg till hus
            nytthus = meny.createHus()
            #print(f"Husnr= {nytthus.husnr} förnamn {nytthus.fnamn} efter namn {nytthus.epost}  Tel {nytthus.tel}")
            db_handler.add_hus(nytthus)
            input("\tFortsätta? tryck Enter: ")

        elif val == "3":#Tabort hus
            #print("Val 3")
            #input("\tFortsätta? tryck Enter: ")
            t_husnr =  meny.printDeleteHus()
            db_handler.deleteHus(t_husnr)

        elif val == "4":#Update hus
            print("Val 4 updatera hus")
            input("\tFortsätta? tryck Enter: ")
            
        elif val == "5":#lista fakturor
            print("Val 5 lista fakturor")
            input("\tFortsätta? tryck Enter: ")
        
        elif val == "6":#lägg till fatura
            nyfaktura = meny.createFaktura()
            db_handler.add_faktura(nyfaktura)
            #print("Val 6 add fakura")
            #input("\tFortsätta? tryck Enter: ")
        
        elif val == "7":#delete faktura
            print("Val 7 tabort fakura")
            input("\tFortsätta? tryck Enter: ")
        
        elif val == "8":#Update fakura
            print("Val 8 updatera faktura")
            input("\tFortsätta? tryck Enter: ")
        
        elif val == "9":#Avsluta
            break

        else:
            print("Ogiltig inmatning!")
          

main()











'''
resultat = df[df['Referens'] == '145']
print(f"Söker hus 145: {resultat}")

totalt_belopp = df['Belopp'].sum()
print(f"Totalt belopp: {totalt_belopp}")


mitthus = hus.Hus("145", "Jens", "Lodin", "jensa@gmail.com", "07068400")
granne = hus.Hus("147", "Henrik", "From", "henrik@gmail.com", "07068200")

print(f"husNr={mitthus.husnr} Namn={mitthus.fnamn} {mitthus.enamn} Mail={mitthus.epost} Tel={mitthus.tel}")
print(f"husNr={granne.husnr} Namn={granne.fnamn} {granne.enamn} Mail={granne.epost} Tel={granne.tel}")
'''
