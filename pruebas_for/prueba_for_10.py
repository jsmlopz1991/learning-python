
numero = input("Dime un numero (FIN para terminar)")
lista = []
valor = 0


while numero != "FIN":
    while not numero.isdigit():
        numero = input("Tiene que ser un numero (FIN para terminar)")
    lista.append(int(numero))
    numero = input("Dime un numero (FIN para terminar)")

valor = len(lista)
total = 0
for recorrer in lista:
    total += recorrer

print("La media es {}".format(total / valor))