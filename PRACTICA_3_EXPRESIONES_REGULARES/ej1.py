import re
pat ="[a-zA-Z0-9]"
txt ="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet"
def verifyText():
    if re.search(pat,txt):
        print("Verificado")
    else: 
        print("No verificado")