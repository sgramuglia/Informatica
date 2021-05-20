class Calculadora:
    def __init__(self):
        self.resultado = 0
    
    def cargar(self, num):
        self.resultado = num
    
    def sumar(self, num):
        self.resultado += num
    
    def restar(self, num):
        self.resultado -= num
    
    def multiplicar(self, num):
        self.resultado = self.resultado * num
    
    def valorActual(self):
        print(self.resultado)

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()