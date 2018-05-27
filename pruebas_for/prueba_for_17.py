
numeros = [1, 2, 3, 4, 5, 15, 123, 23, 434, 54, 64, 75]

for indice in range(len(numeros)):
    posicion = numeros[indice]

    if posicion % 3 == 0:
        numeros[indice] = "Fizz"

    if posicion % 5 == 0:
        numeros[indice] = "Buzz"

    if posicion % 3 == 0 and posicion % 5 == 0:
        numeros[indice] = "Bazinga"


print(numeros)