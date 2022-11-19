lista = ["A", "B", "b", "c", "E", "E", "f"]
print(f"Lista original: {lista}")

elemento = input("Introduce el elemento que deseas eliminar: ")

for _ in lista:
    if elemento.lower() in lista:
        lista.remove(elemento.lower())
    elif elemento.upper() in lista:
        lista.remove(elemento.upper())

print(f"Elemento eliminado: {lista}")
