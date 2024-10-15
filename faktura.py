
class Faktura:

    def __init__(self, fakturanr:str=None, year:int=None, husnr:str=None, belopp:str=None, betalningsstatus:int=None, betalningsdatum:str=None, f_id=None, id=None ):
        
        self.fakturanr = fakturanr
        self.year = year
        self.husnr = husnr
        self.belopp = belopp
        self.betalningsstatus = betalningsstatus
        self.betalningsdatum = betalningsdatum
        self.f_id = f_id
        self.id = id

   

    def get_faktura(self):
        return self 
    
    def set_fakturanr(self, fakturanr:str):
        self.fakturanr = fakturanr

    def set_year(self, year:int):
        self.year = year

    def set_husnr(self, husnr:str):
        self.husnr = husnr

    def set_belopp(self, belopp:str):
        self.belopp = belopp

    def set_betalningsstatus(self, betalningsstatus:str):
        self.betalningsstatus = betalningsstatus

    def set_betalningsdatum(self, betalningsdatum:str):
        self.betalningsdatum = betalningsdatum

    def set_F_id(self, f_id:str):
        self.f_id = f_id