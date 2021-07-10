import pandas as pd

dic = {"Name" : ["Levi","Eren","Armin","Mikasa","Zoe"],
       "Surname" : ["Ackerman","Yeager","Arlert","Ackerman","Hange"],
       }

df = pd.DataFrame(dic)
newdf = pd.DataFrame()

def DeleteRows(n):
    global newdf
    newdf = df.tail(len(df)-n)
    print(newdf)
