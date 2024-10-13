
class Faktura:

    def __init__(self, fakturanr:str=None, year:int=None, husnr:str=None, belopp:str=None, betalningsstatus:int=None, betalningsdatum:str=None, info:str=None, f_id=None, ):
        
        self.fakturanr = fakturanr
        self.year = year
        self.husnr = husnr
        self.belopp = belopp
        self.betalningsstatus = betalningsstatus
        self.betalningsdatum = betalningsdatum
        self.info = info
        self.f_id = f_id

   

    def get_faktura(self):
        return self 
    
    def set_fakturanrnr(self, fakturanr:str):
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

    def set_info(self, info:str):
        self.info = info