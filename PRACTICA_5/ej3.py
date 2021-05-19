class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento(self, num):
        des = (num/100) * self.precio
        return (self.precio - des)

n1 = Notebook("Lenovo" , "Chuchi" , "2000000")
print(n1.descuento(40))

