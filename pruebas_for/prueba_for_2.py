frase = input("Dime una frase: ")

mayusculas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "X", "Y", "Z"]
numero_mayusculas = 0

for recorrido in frase:
    for mayus in mayusculas:
        if recorrido == mayus:
            numero_mayusculas += 1

print("El numero de mayusculas es {} ".format(numero_mayusculas))
