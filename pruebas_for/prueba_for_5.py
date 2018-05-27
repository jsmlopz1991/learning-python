numero =input("Dime el numero a evaluar: ")

while not numero.isdigit():
    numero = input("Eso no es un número, dime que numero quieres evaluar: ")

numero = int(numero)

for multiplicar in range(1,11):
    if multiplicar % 2 == 0:
        print("{} x {} es {}".format(numero, multiplicar, numero * multiplicar))
