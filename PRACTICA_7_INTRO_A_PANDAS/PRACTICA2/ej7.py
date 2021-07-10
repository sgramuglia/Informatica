import pandas as pd

dicC1 = {"Name":["Juana","Pedro","Carlos"],"Math":[10,8.5,6],"Literature":[9,7,8],"Biology":[7,7,8]}
class1 = pd.DataFrame(dicC1)

englishMarks = [7,6,8]

class1["English"] = englishMarks
