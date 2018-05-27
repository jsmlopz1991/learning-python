numero = input("Dime de que numero quieres monstrar la tabla ")

while not numero.isdigit():
    numero = input("Eso no es un número, dime de que numero quieres monstrar la tabla ")

numero = int(numero)

for multiplicar in range(5,16):
    print("{} x {} es {}".format(numero, multiplicar, numero * multiplicar))