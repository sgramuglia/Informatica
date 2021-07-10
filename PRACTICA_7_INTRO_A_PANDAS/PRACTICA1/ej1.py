import pandas as pd
l1 = [3, 7, 12, 15, 21]
l2 = [1, 4, 10, 14, 19]
s1 = pd.Series(l1)
s2 = pd.Series(l2)

sum = (s1 + s2)
sub = (s1 - s2)
mult = (s1 * s2)
div = (s1 / s2)

print(sum)
print(sub)
print(mult)
print(div)