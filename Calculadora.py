print("********************")
print("* Menu de opciones *")
print("********************")

print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")
print("5. Division entera")
print("6. Exponente")
print("7. Modulo o resto \n")

numero = int(input("Introduce la opcion deseada: "))

if numero == 1:

    print("Elegiste suma \n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es:",numero)

elif numero == 2:

    print("Elegiste resta \n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es:",numero)

elif numero == 3:

    print("Elegiste multiplicacion \n")
    numero = int(input("Introduce el primer numero: "))
    numero *= int(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicacion es:",numero)

elif numero == 4:

    print("Elegiste division \n")
    numero = float(input("Introduce el primer numero: "))
    numero /= int(input("Introduce el segundo numero: "))
    print("El resultado de la division es:",round(numero, 2))

elif numero == 5:

    print("Elegiste division entera \n")
    numero = int(input("Introduce el primer numero: "))
    numero //= int(input("Introduce el segundo numero: "))
    print("El resultado de la division entera es:",numero)

elif numero == 6:

    print("Elegiste exponente \n")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado de la exponente es:",numero)

elif numero == 7:

    print("Elegiste modulo o resto \n")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El modulo o resto es:",numero)

else:
    print("La opcion que elegiste no existe, vuelve a intentarlo")

