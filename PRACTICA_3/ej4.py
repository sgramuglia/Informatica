import re
txt = "Amet_et_amet"
pat ="[a-zA-Z]_[a-zA-Z]"
if re.search(pat,txt):
    print("unida con guión bajo")