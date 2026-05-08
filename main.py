#2-misil
class Talaba:
    def __init__(self, fullname, ball):
        self.fullname = fullname
        self.ball = ball
        self.__ball = 0

    def ball_qosh(self, qiymat):
        self.__ball += qiymat

    def info(self):
        print(f"ismi: {self.fullname}")
        print(f"bali: {self.ball}")

t1 = Talaba("Dilnura", "100")
t1.info()


#3-misol
class BamkHisob:
    def __init__(self, egasi, balans):
        self.egasi = egasi
        self.balans = balans
        self.__balans = 0

    def pul_qosh(self, summa):
        self.__balans += summa

    def pul_yech(self, summa):
        self.__balans -= summa

    def info(self):
        print(f"egasi: {self.egasi}")
        print(f"Balansi: {self.balans}")

b1 = BamkHisob("Sevinch", "200")
b1.info()


#4-misol
class Telefon:
    def __init__(self, model, batareya):
        self.model = model
        self.batareya = batareya
        self.__batareya = 0

    def zaryad_qil(self, foiz):
        self.__batareya += foiz

    def foydalan(self, foiz):
        self.__batareya -= foiz

    def info(self):
        print(f"Modeli: {self.model}")
        print(f"Batargiyasi: {self.__batareya}")

t1 = Telefon
