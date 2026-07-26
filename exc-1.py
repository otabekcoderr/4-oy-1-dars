class Telefon:
    def __init__(self,model,xotira,batareyka):
        self.model = model
        self.xotira = xotira
        self.batareyka = batareyka
    def info(self):
        print(f"Barcha ma'lumotlar: Model: {self.model}\nXotira: {self.xotira} GB\nBatareyka: {self.batareyka} mAh")
    def zaryad_yetarlimi(self,soat):
        mAh = 200*soat
        if mAh<self.batareyka:
            print(f"Yo'q yetarli emas! {soat} uchun {mAh} kerak. Sizda {self.batareyka} mAH bor")
        else:
            print("Yetarli!")
telefon = Telefon("Opus 4.6",512,3200)
telefon.info()
soat = int(input("Soat kiriting"))
telefon.zaryad_yetarlimi(soat)
