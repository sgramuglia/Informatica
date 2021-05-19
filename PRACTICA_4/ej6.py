import re
import shutil
route = r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt"
newRoute = r"C:\Users\sofig\Desktop\info\Informatica\txtsaltos.txt"
with open(route,"r") as txt:
    originalFile = txt.read()
with open(newRoute,"w") as newFile:
    shutil.copyfile(route,newRoute)
with open(newRoute,"r+") as alteredFile:
    #alteredFile.write(re.sub("^\n", " ", alteredFile.read()))
    for line in alteredFile:
        line = line.replace("\n", "")