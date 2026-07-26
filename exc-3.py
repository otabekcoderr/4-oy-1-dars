class Server:
    def __init__(self,nom,ram,disk):
        self.nom = nom
        self.ram = ram
        self.disk = disk
    def texnik_malumot(self):
        print(f"Barcha ma'lumotlar:\nNom {self.nom}\nRam: {self.ram}\nDisk: {self.disk}")
    def saralash(self,hajm):
        cal = hajm/1024
        if self.disk<cal:
            print(f"{hajm} GB fayl {self.disk} TB diskga sig'maydi")
        else:
            print(f"{hajm} GB fayl {self.disk} TB diskga sig'adi")
servers = Server("MainServer", 64, 2)
servers.texnik_malumot()
hajm = int(input("File hajmini kiriting"))
servers.saralash(hajm)