import pandas as pd

def CheckColl(coll,df):
  try:
    print(df[coll])
  except:
    print("There is no collumn defined as" + coll + "in the submitted DataFrame")
