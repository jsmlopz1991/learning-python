pregunta = input("Dime una frase: ")
numero = 0

for cambiar in pregunta:
    if cambiar == "a" or cambiar == "e" or cambiar == "i" or cambiar == "o" or cambiar == "u":
        pregunta1 = pregunta.find(cambiar) + 1
        pregunta1 = str(pregunta1)
        pregunta = pregunta.replace(cambiar, pregunta1, 1)

print(pregunta)
