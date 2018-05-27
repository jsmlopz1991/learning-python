#Variables por defecto
nombre_pokemon = str.upper("pikachu")
vida_pikachu = 85
vida_pokemon = 0
ataque = 0
pokemon_enemigo = str.upper(input("Que pokemon contra el que luchar escoges? (Bulbasaur/Charmander/Squirtle): "))

while pokemon_enemigo != "BULBASAUR" and pokemon_enemigo != "CHARMANDER" and pokemon_enemigo != "SQUIRTLE":
        pokemon_enemigo = str.upper(input("No reconozco a ese pokemon, solo puedes elegir estos(Bulbasaur/Charmander/Squirtle): "))

if "BULBASAUR" == pokemon_enemigo:
    vida_pokemon = 100
    ataque = 10


elif "CHARMANDER" == pokemon_enemigo:
    vida_pokemon = 80
    ataque = 7


elif "SQUIRTLE" == pokemon_enemigo:
    vida_pokemon = 90
    ataque = 8

while vida_pikachu > 0 and vida_pokemon > 0:
    ataque_usado = str.upper(input("Que ataque quieres usar? (Chispazo, 10 de daño/Bolazo, 12 de daño): "))

    while ataque_usado != "CHISPAZO" and ataque_usado != "BOLAZO":
        ataque_usado = str.upper(input("No conozco ese ataque, elige uno de estos (Chispazo, 10 de daño/Bolazo, 12 de daño): "))

    if ataque_usado == "CHISPAZO":
        ataque_pikachu = 10

    else:
        ataque_pikachu = 12

    vida_pokemon -= ataque_pikachu
    vida_pikachu -= ataque
    print("Tras el ataque de {} puntos de daño de {} la vida de {} ahora es {} puntos de vida".format(ataque, pokemon_enemigo, nombre_pokemon, vida_pikachu))
    print("Tras el ataque de {} puntos de daño de {} la vida de {} es de {} puntos de vida".format(ataque_pikachu, nombre_pokemon, pokemon_enemigo, vida_pokemon))

    if vida_pokemon <= 0:
        print("Has ganado {}".format(nombre_pokemon))

    elif vida_pikachu <= 0:
        print("Has perdido contra {}".format(pokemon_enemigo))
