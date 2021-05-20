class Contador:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
    
    def inc(self):
        self.valor += 1
    
    def dis(self):
        self.valor -= 1
    
    def reset(self):
        self.valor = 0
    
    def valorActual(self):
        print(self.valor)
    
    def valorNuevo(self, valor_nuevo):
        self.valor = valor_nuevo
        print(self.valor)

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()
