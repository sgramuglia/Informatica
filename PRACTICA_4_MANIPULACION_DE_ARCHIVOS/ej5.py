import re
import shutil
route = r"C:\Users\sofig\Desktop\info\Informatica\txtmanip.txt"
newRoute = r"C:\Users\sofig\Desktop\info\Informatica\newtxtmanip.txt"
with open (route,"r") as txt:
    data = txt.read()
with open (newRoute,"w") as txt2:
    shutil.copyfile(route,newRoute)
with open (newRoute,"r+") as copy:
    copy.write(re.sub("s", "s\n",copy.read()))