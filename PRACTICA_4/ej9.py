import re
import string
frequency = {}
txt = open(r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt", "r")

data = txt.read()
w = data.split()
wcount = len(w)

match_pattern = re.findall(r'\b[a-z]{3,15}\b', data.lower())


for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    fr = frequency[words]/wcount
    print(words, fr)