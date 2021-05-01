import re
txt = input("Insertar cadena de texto: ")
noneOrMore = "he*"
oneOrMoreE = "he+"
twoOrThreeE = "he{2,3}"
re.search(noneOrMore,txt)
re.search(oneOrMoreE,txt)
re.search(twoOrThreeE,txt)
