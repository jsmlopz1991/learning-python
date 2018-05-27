lista_mixta = [10, 3, 4, 5, "asd", "hola", "lucia", "papa", "patatas", "cinco", 1, 2, 2.1]

lista_strings = []
lista_enteros = []

for recorrido in lista_mixta:
    if type(recorrido) == int:
        lista_enteros.append(recorrido)
    elif type(recorrido) == str:
        lista_strings.append(recorrido)

print("La lista de strings es la siguiente {}".format(lista_strings))
print("La lista de enteros es la siguiente {}".format(lista_enteros))