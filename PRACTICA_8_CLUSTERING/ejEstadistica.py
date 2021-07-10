import pandas as pd

dt = pd.read_csv("C:\Info\Datos.csv")

dtNoNan = dt.dropna()
dtHeight = dtNoNan[dtNoNan["Altura"] < 2.2]
dtHeight.plot.scatter("Nombres","Sueldo")
dtFinal = dtHeight[dtHeight["Sueldo"] < 150000]

dtFinal["Sueldo"].mode()
dtFinal["Altura"].mode()

dtFinal["Sueldo"].plot.density()
dt["Altura"].plot.density()