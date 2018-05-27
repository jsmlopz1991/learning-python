operacion = str.upper(input("¿Que operacion quieres realizar?(multiplicar / dividir / sumar / restar): "))
primer_numero = int(input("Dime el primer numero: "))
segundo_numero = int(input("Dime el segundo numero: "))

if operacion == "MULTIPLICAR":
    resultado=primer_numero * segundo_numero
elif operacion == "DIVIDIR":
    resultado =primer_numero / segundo_numero
elif operacion == "SUMAR":
    resultado =primer_numero + segundo_numero
elif operacion == "RESTAR":
    resultado =primer_numero - segundo_numero

print("El resultado de {} {} con {} es {}".format(operacion, primer_numero, segundo_numero, resultado))
