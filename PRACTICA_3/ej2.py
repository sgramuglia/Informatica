import re
pat = "\W"
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet"
txt = "Amet@amet"
def verifyText(text):
    if not(re.search(pat,text)):
        print("Verificado")
    else: 
        print("No verificado")