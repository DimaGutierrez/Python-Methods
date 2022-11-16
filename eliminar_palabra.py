string = input("Introduce una frase: ")
palabra = input("Introduce la palabra que deseas eliminar: ")
substring = ""

indice = string.find(palabra)
substring = string[0 : indice] + string[indice + len(palabra) + 1 : ]

print(f"Cadena resultante: {substring}")
