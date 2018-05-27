pregunta = input("Dime una frase: ")
numero = 0

for cambiar in pregunta:
    if cambiar == "a" or cambiar == "e" or cambiar == "i" or cambiar == "o" or cambiar == "u":
        pregunta = pregunta.replace(cambiar, "i")

print(pregunta)