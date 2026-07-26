import random
import time


class Svetafor:
    def __init__(self, tugma, chiroq):
        self.tugma = tugma
        self.chiroq = chiroq

    def chiraq_yoq(self):
        # sum = 0
        while True:
            if self.chiroq == "qizil" and self.tugma == "1":
                time.sleep(1)
                print(
                    "🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥   Piyodalar\n🟥🟥🟥🟥🟥   o'tishi\n🟥🟥🟥🟥🟥   mumkin\n🟥🟥🟥🟥🟥\n"
                )
                time.sleep(5)
                print(
                    "🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩   Mashinalar\n🟩🟩🟩🟩🟩   harakatlanmoqda\n🟩🟩🟩🟩🟩   To'xtang!!!\n🟩🟩🟩🟩🟩\n"
                )
                time.sleep(5)
                print(
                    "🟨🟨🟨🟨🟨\n🟨🟨🟨🟨🟨   Mashinalar\n🟨🟨🟨🟨🟨   to'xtamoqda!\n🟨🟨🟨🟨🟨   shoshmang!!!\n🟨🟨🟨🟨🟨\n"
                )
                time.sleep(1)
                # sum+=1

            elif self.chiroq == "sariq" and self.tugma == "1":
                time.sleep(1)
                print(
                    "🟨🟨🟨🟨🟨\n🟨🟨🟨🟨🟨   Mashinalar\n🟨🟨🟨🟨🟨   to'xtamoqda!\n🟨🟨🟨🟨🟨   shoshmang!!!\n🟨🟨🟨🟨🟨\n"
                )

                button = input("Qatnov to'xtatish tugmasi: (1)\n")
                time.sleep(2)
                print(
                    "🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥   Piyodalar\n🟥🟥🟥🟥🟥   o'tishi\n🟥🟥🟥🟥🟥   mumkin\n🟥🟥🟥🟥🟥\n"
                )
                time.sleep(5)
                print(
                    "🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩   Mashinalar\n🟩🟩🟩🟩🟩   harakatlanmoqda\n🟩🟩🟩🟩🟩   To'xtang!!!\n🟩🟩🟩🟩🟩\n"
                )
                time.sleep(5)
                # sum+=1

            elif self.chiroq == "yashil" and self.tugma == "1":
                time.sleep(1)
                print(
                    "🟩🟩🟩🟩🟩\n🟩🟩🟩🟩🟩   Mashinalar\n🟩🟩🟩🟩🟩   harakatlanmoqda\n🟩🟩🟩🟩🟩   To'xtang!!!\n🟩🟩🟩🟩🟩\n"
                )

                button = input("Qatnov to'xtatish tugmasi: (1)\n")
                time.sleep(2)
                print(
                    "🟨🟨🟨🟨🟨\n🟨🟨🟨🟨🟨   Mashinalar\n🟨🟨🟨🟨🟨   to'xtamoqda!\n🟨🟨🟨🟨🟨   shoshmang!!!\n🟨🟨🟨🟨🟨\n"
                )
                time.sleep(2)
                print(
                    "🟥🟥🟥🟥🟥\n🟥🟥🟥🟥🟥   Piyodalar\n🟥🟥🟥🟥🟥   o'tishi\n🟥🟥🟥🟥🟥   mumkin\n🟥🟥🟥🟥🟥\n"
                )
                time.sleep(5)
                # sum+=1 -  Sikl 2 marta aylanganda to'xtatish uchun ishlatgandim lekin cheksiz aylantirishni tanladim!Hurmatli AI


svetafor_chiroq = ("qizil", "sariq", "yashil")
chiroq = random.choice(svetafor_chiroq)
# tugma_num = int(input("Piyodalar o'tishini so'rash uchun 1ni bosing"))
tugma = Svetafor("1", chiroq)
tugma.chiraq_yoq()


# BU dasturni Toshkentdagi yangi svetaforlardan ilhomlanib yaratdim yani piyodalar o'tishni hohlaganda tugma bosadi svetafor esa o'z kerakli vaqtda to'xtaydi, dasturda kamchiliklar bor texnik bilimim yetmadi to'g'irlashga
