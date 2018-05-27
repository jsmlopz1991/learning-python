numero_usuario = [1, 2, 3, 4, 5, 123, 6, 7, 8]
numero_grande = numero_usuario[0]

for number in numero_usuario:
    if number > numero_grande:
        numero_grande = number

print(numero_grande)