
numero = input("Dime un numero (FIN para terminar)")
lista = []
valor = 0


while numero != "FIN":
    while not numero.isdigit():
        numero = input("Tiene que ser un numero (FIN para terminar)")
    lista.append(numero)
    numero = input("Dime un numero (FIN para terminar)")


for recorrer in lista:
    valor +=1

print("El largo de la lista es {}".format(valor))