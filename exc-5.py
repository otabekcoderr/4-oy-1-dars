class Bugtracker:
    def __init__(self, loyiha_nomi="", xatolar=[], dasturchi=""):
        self.loyiha_nomi = loyiha_nomi
        self.xatolar = xatolar
        self.dasturchi = dasturchi

    def xato_qoshish(self, xato):
        self.xatolar.append(xato)

    def hisobot(self):
        sum = 0
        print(f"Loyiha: {self.loyiha_nomi} | Dasturchi: {self.dasturchi}")
        print("Xatolar:")
        for i in self.xatolar:
            sum += 1
            print(f"{sum}. {i}")


b = Bugtracker("OnlineShop", [], "Vali")
b.xato_qoshish("Login sahifasi ishlamaydi")
b.xato_qoshish("To'lov xatosi")

b.hisobot()
