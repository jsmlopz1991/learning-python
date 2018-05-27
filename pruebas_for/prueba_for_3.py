frase = input("Dime una frase: ")

vocales = []

for recorrido in frase:
    if recorrido == "a" or recorrido == "e" or recorrido == "i" or recorrido == "o" or recorrido == "u":
        vocales.append(recorrido)

print("Las vocales son {} ".format(vocales))