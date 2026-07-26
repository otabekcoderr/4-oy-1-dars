class Vebsayt:
    def __init__(self,domen,til,oylik_tashrif):
        self.domen = domen
        self.til = til
        self.oylik_tashrif = oylik_tashrif
    def info(self):
        print(f"Domen: {self.domen}\nTil: {self.til}\nOylik tashrif: {self.oylik_tashrif}")
    def mashhurlik(self):
        if 10000>self.oylik_tashrif:
            print("Boshlkang'ich")
        elif 10000<self.oylik_tashrif<100000:
            print("O'rta")
        elif 100000<=self.oylik_tashrif:
            print("Mashhur")
sayt = Vebsayt("Kitobchi.uz","HTLM,Css,JavaScript",100000)
sayt.info()
sayt.mashhurlik()