numero = input("Dime de que numero quieres mostrar la tabla ")

while not numero.isdigit():
    numero = input("Eso no es un número, dime que numero quieres evaluar: ")

numero = int(numero)
for multiplicar in reversed(range(1,11)):
    print("{} x {} es {}".format(numero, multiplicar, numero * multiplicar))
