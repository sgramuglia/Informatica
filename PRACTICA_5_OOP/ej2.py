class Golondrina:
    def __init__(self,energia):
        self.energia = energia

    def comer_alpiste(self,gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        if (10 + kms < self.energia):
            self.energia -= 10 + kms
        else: 
            print("No tiene suficiente energía")

    def esta_debil(self):
        return self.energia <= 10

pepita = Golondrina(200)
pepita.volar(50)
print(pepita.energia)
pepita.volar(100)
