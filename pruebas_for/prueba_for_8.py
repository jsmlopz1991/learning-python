
numero_usuario = []
numero = ""

while len(numero_usuario) < 4:
    while not numero.isdigit():
        numero = input("Dime el numero a introducir: ")
    numero_usuario.append(int(numero))
    print("Has añadido el número correctamente!")
    numero = input("Dime el numero a introducir: ")


numero_pequeno = numero_usuario[0]

for number in numero_usuario:
    if number < numero_pequeno:
        numero_pequeno = number

print("El número más pequeño es: {} ".format(numero_pequeno))