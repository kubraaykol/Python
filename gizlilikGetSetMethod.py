class Araba:
    def __init__(self, model):
        self.renk = "kırmızı"
        self.model = model

class Fiat(Araba):
    def __init__(self, yil):
        self.__beygirGucu = 95
        super().__init__(yil)
        print(self.renk)

    def getBeygirGucu(self):
        return self.__beygirGucu

# Nesne oluşturma ve method çağrısı sınıf tanımlamalarının dışında olmalıdır.
fiat = Fiat(2024)
print(fiat.getBeygirGucu())
