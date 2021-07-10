import pandas as pd

l1 = [3, 7, 9, 14, 25]
l2 = [1, 7, 10, 16, 19]
s1 = pd.Series(l1).bool()
s2 = pd.Series(l2).bool()

grtr = s1 > s2
lesser = s1 < s2
eq = (s1 == s2)

if grtr:
    print(s1 + "is greater than" + s2)
else:
    print(s2 + "is greater than" + s1)

if lesser:
    print(s1 + "is less than" + s2)
else:
    print(s2 + "is less than" + s1) 

if eq: 
    print(s1 + "and" + s2 + "are equal")

