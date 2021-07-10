import pandas as pd

emptydf = pd.DataFrame()

def Addcoll(header , dt):
  emptydf[header] = dt

def Addrow(index , dt):
  emptydf.loc[index] = dt

Addcoll("name", ["Levi","Eren","Armin","Mikasa","Zoe"])
Addcoll("surname", ["Ackerman","Yeager","Arlert","Ackerman","Hange"])

