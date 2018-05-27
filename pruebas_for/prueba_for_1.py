
frase = input("Dime una frase: ")
puntos = 0
comas = 0
espacios = 0

for recorrido in frase:
    if recorrido == " ":
        espacios += 1
    elif recorrido == ".":
        puntos += 1
    elif recorrido == ",":
        comas += 1

print("Espacios: {}".format(espacios))
print("Puntos: {}".format(puntos))
print("Comas: {}".format(comas))