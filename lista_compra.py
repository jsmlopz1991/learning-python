
mi_lista = []
input_usuario = ""

input_usuario=input("¿Que necesitas comprar? (Escribe FIN para terminar): ")
while input_usuario != "FIN":
    mi_lista.append(input_usuario)
    input_usuario=input("¿Que necesitas comprar? (Escribe FIN para terminar): ")

print("Esta es la lista de la compra")
for item in mi_lista:
    print("Hay que comprar {} ".format(item))