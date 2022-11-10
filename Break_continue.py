#Ejemplo para Break

print("While con centencia break \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print("valor actual de la variable: ", contador)

print("Fin del programa, la sentencia break se ha ejecutado \n")

#Ejemplo para continue

print("\While con centencia continue \n")
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print("valor actual de la variable: ", contador)



