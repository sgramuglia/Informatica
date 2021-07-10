import pandas as pd

dt = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
lbl = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(data = dt, index = lbl)

newdf = pd.DataFrame(data=[df["nombre"],df["puntaje"]]).transpose()

dic = {"mayusname":[],"length":[]}

for name in list(newdf["nombre"]):
  dic["mayusname"].append(name.upper())

for name in dic["mayusname"]:
  dic["length"].append(len(name))

finaldf = pd.DataFrame(dic)