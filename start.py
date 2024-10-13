import pandas as pd
import hus
import faktura
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

            
            print("Val 1")
            input("\tFortsätta? tryck Enter: ")
            #lista_motorcyklar = mc_handler.readSqliteTable()
            #mc = motorcykel_app_menu.printListMotorcykel(lista_motorcyklar)
            
        elif val == "2":#lägg till motrcyke
            nytthus = meny.createHus()
            print(f"Husnr= {nytthus.husnr} förnamn {nytthus.fnamn} efter namn {nytthus.epost}  Tel {nytthus.tel}")
            db_handler.add_hus(nytthus)
            #mc_handler.addMotorcykel(mc)
            print("Val 2")
            input("\tFortsätta? tryck Enter: ")

        elif val == "3":#Tabort motorcykel
            #t_id =  motorcykel_app_menu.printDeleteMotorcykel()
            #mc_handler.deleteMotorcykel(t_id)
            print("Val 3")
            input("\tFortsätta? tryck Enter: ")
        
        elif val == "4":#Avsluta
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
