print("=========")
print("conversor")
print("========= \n")

print("Menu de opciones: \n")
print("Presiona 1 para convertir de numero a palabra")
print("Presiona 2 para convertir de palabra a numero \n")

opcion = int(input("Cual es tu opcion deseada?: "))

if opcion == 1:
    print("\n Conversor de numero a palabra. \n")

    opcion_uno = int(input("cual es el numero que deseas convertir a palabra?: "))

    if opcion_uno == 1:
        print("el numero es 'UNO'")
    elif opcion_uno == 2:
        print("el numero es 'Dos'")
    elif opcion_uno == 3:
        print("el numero es 'Tres'")
    elif opcion_uno == 4:
        print("el numero es 'Cuatro'")
    elif opcion_uno == 5:
        print("el numero es 'Cinco'")
    else:
        print("El numero registrado no existe")
    
elif opcion == 2:
    print("\n Conversor de palabra a numero. \n")

    opcion_dos = int(input("cual es la palabra que deseas convertir a numero?: "))

    if opcion_dos == uno:
        print("el numero es '1'")
    elif opcion_dos == dos:
        print("el numero es '2'")
    elif opcion_dos == tres:
        print("el numero es '3'")
    elif opcion_dos == cuatro:
        print("el numero es '4'")
    elif opcion_dos == cinco:
        print("el numero es '5'")
    else:
        print("la palabra registrada no existe")

else:
    print("Opcion no disponible")

print("Fin.")


