class Contador:
    def __init__(self, valor_inicial):
        self.valor = valor_inicial
        self.memory = valor_inicial
    
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

    def ultimoComando(self):
        if self.valor == self.memory + 1:
            print("incremento")
            self.memory += 1
        elif self.valor == 0:
            print("reset")
        elif self.valor == self.memory - 1:
            print("disminución")
            self.memory -=1
        else:
            print("actualización")


cont = Contador(10)
cont.valorNuevo(40)
cont.ultimoComando()
cont.inc()
cont.ultimoComando()
cont.dis()
cont.ultimoComando()
cont.res()
cont.ultimoComando()