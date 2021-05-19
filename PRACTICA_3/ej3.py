import re
txt = input("Insertar cadena de texto: ")
noneOrMore = "he*"
oneOrMoreE = "he+"
twoOrThreeE = "he{2,3}"
if re.search(noneOrMore,txt):
    print("ninguna una o mas")
elif re.search(oneOrMoreE,txt):
    print("una o mas")
elif re.search(twoOrThreeE,txt):
    print("dos o tres")
