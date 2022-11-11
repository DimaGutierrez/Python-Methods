string = "Menú"

print("Métodos con espacios:")
print(string.center(20))
print(string.ljust(20))
print(string.rjust(20))

print("\nMétodos con caracter:")
print(string.center(20, "="))
print(string.ljust(20, "="))
print(string.rjust(20, "="))

print("\nVariable modificada:")
string = string.center(10, "=")
print(string)
