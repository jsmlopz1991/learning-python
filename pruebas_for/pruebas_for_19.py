
numeros = [1, 2, 3, 4, 5, 15, 123, 23, 434, 54, 64, 75]

lista_2 = []
lista_3 = []
lista_5 = []
lista_7 = []

for indice in range(len(numeros)):
    posicion = numeros[indice]

    if posicion % 2 == 0:
        lista_2.append(posicion)

    if posicion % 3 == 0:
        lista_3.append(posicion)

    if posicion % 5 == 0:
        lista_5.append(posicion)

    if posicion % 7 == 0:
        lista_7.append(posicion)

    if posicion % 3 == 0 and posicion % 5 == 0 and posicion % 7 == 0:
        lista_3.append(posicion)
        lista_5.append(posicion)
        lista_7.append(posicion)


print(numeros)
print("Multiplos de 2 {} . Multiplos de 3 {}. Multiplos de 5 {}. Multiplos de 7{}".format(lista_2, lista_3, lista_5, lista_7))