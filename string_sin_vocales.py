string = input("Introduce una frase: ")
letter = input("¿Con que frase deseas terminar el bucle?: ")

for character in string:
    if character.lower() == letter.lower():
        break
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    print(character, end="")
