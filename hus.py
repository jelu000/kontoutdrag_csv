class Hus:
    def __init__(self, husnr:str=None , fnamn:str=None, enamn:str=None, epost:str=None, tel:str=None, id=None):
        self.id = id
        self.husnr = husnr
        self.fnamn = fnamn
        self.enamn = enamn
        self.epost = epost
        self.tel = tel
        
    def add_hus(self, husnr, fnamn, enamn, epost, tel):
        self.husnr = husnr
        self.fnamn = fnamn
        self.enamn = enamn
        self.epost = epost
        self.tel = tel

    def __str__(self):
        return self
        #return f"Hus (ID: {self.id}) på {self.gata} {self.husnummer}, {self.postort}"

    def get_hus(self):
        return self 
    
    def set_husnr(self, husnr:str):
        self.husnr = husnr

    def set_fnamn(self, fnamn:str):
        self.fnamn = fnamn

    def set_enamn(self, enamn:str):
        self.enamn = enamn

    def set_epost(self, epost:str):
        self.epost = epost

    def set_tel(self, tel:str):
        self.tel = tel
# Exempel på användning:
#hus1 = Hus(1, "Storgatan", "12", "123 45", "Stockholm")
#print(hus1)

# Lägg till en person som bor i huset:
'''class Person:
    def __init__(self, namn, efternamn):
        self.namn = namn
        self.efternamn = efternamn
'''
'''person1 = Person("Kalle", "Svensson")
hus1.add_boende(person1)'''

# Skriv ut information om huset och dess boende
#print(hus1)
#for person in hus1.boende:
 #   print(f"- {person.namn} {person.efternamn}")





'''class Hus:

    def __init__(self, id=None, fabrikat=None, modell=None, kubik=None, vikt=None, hk=None, topphastighet=None):
        self.id = id
        self.fabrikat = fabrikat
        self.modell = modell
        self.kubik = kubik
        self.vikt = vikt
        self.hk = hk
        self.topphastighet = topphastighet
'''
   

    