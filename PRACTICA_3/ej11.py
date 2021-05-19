import re
lstr = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
for w in lstr:
    ans = re.match("(P\w*)\W(P\w*)", w)
    if ans is not None:
        print(ans.group())