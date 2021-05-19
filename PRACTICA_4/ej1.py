import re
route = r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt"
i = 0
with open(route,"r") as txt:
    if not(re.search("^W",txt)):
        i += 1