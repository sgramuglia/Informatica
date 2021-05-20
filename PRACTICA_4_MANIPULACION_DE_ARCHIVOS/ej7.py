import re
route = r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt"
with open(route, 'r') as infile:
    txt = infile.read().split()
    max_len = len(max(txt, key=len))
    longest = [word for word in txt if len(word) == max_len]
    longest = re.split("[^a-zA-Z\d]+", str(longest))
    longest = ','.join([ i for i in longest if len(i) > 0 ])
    print(longest)
    print(len(longest))
