vocales = ["a", "e", "i", "o", "u"]
print(f"Listas: {vocales}")
del vocales[3]
print(f"del vocales[3]: {vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nListas: {vocales}")
del vocales[0:2]
print(f"del vocales[0:2]: {vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nListas: {vocales}")
del vocales[:]
print(f"del vocales[:]: {vocales}")

vocales = ["a", "e", "i", "o", "u"]
print(f"\nListas: {vocales}")
del vocales
print(f"del vocales: {vocales}")
