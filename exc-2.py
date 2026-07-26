class Dasturchi:
    def __init__(self,ism,til,tajriba):
        self.ism = ism
        self.til = til
        self.tajriba = tajriba
    def taqdimot(self):
        print(f"Mening ismim {self.ism}, {self.til} dasturchisiman va {self.tajriba} yillik tajribaga egaman ...")
    def is_haqqi(self):
        haq = self.tajriba*500
        print(f"Oylik ish haqqingiz: {haq} $")
coder = Dasturchi("Otabek","Python",3)
coder.taqdimot()
coder.is_haqqi()
