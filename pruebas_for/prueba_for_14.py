pregunta = input("Dime la cadena de texto a formatear: ")
str_reemplazo = "VACA"

for cambiar in pregunta:
    if cambiar == "a" or cambiar == "A":
        pregunta1 = pregunta.replace(cambiar, str_reemplazo)

print(pregunta1)