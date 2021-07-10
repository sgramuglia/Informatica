import pandas as pd

dicC1 = {"Name":["Juana","Pedro","Carlos"],"Math":[10,8.5,6],"Literature":[9,7,8],"Biology":[7,7,8]}
dicC2 = {"Name":["Luis","Martina","Camila"],"Math":[9,7,5.5],"Literature":[10,8,7],"Economy":[9,8,7]}

class1 = pd.DataFrame(dicC1)
class2 = pd.DataFrame(dicC2)

mergedDf = pd.concat([class1,class2] , ignore_index = True , axis = 0)
