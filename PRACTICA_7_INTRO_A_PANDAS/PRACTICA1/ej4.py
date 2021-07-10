import pandas as pd

d1 = {"a": [1,3,5,2], "b": [4,2,3,5]}
d2 = {}
for key in d1.keys():
  d2[key] = []
  for n in d1[key]:
    if d1[key].index(n)%2 == 0:
      d2[key].append(n ** d1[key][(d1[key].index(n))+1])