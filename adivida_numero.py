import os
import platform

operative_system = platform.system()
correcto=input("Numero a adivinar:")

if operative_system == "Windows":
    os.system('cls')
else:
    os.system('clear')


aleatorio=input("Adivina el numero: ")

while correcto != aleatorio:
    print("No es el numero correcto, vuelve a intentarlo")
    aleatorio = input("Adivina el numero: ")
print("Has acertado!")
