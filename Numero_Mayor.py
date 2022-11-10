print("*********************************************************")
print("* Programa para determinar cual es el munero mas grande *")
print("*********************************************************")

num_uno = int(input("Introduce el primer numero:"))
num_dos = int(input("Introduce el segundo numero:"))
num_tres = int(input("Introduce el tercer numero:"))

if num_uno > num_dos and num_uno > num_tres:
    print("El numero ", num_uno, " es el numero mas grande de los tres.")
else:
    if num_dos > num_tres:
        print("El numero ", num_dos, " es el numero mas grande de los tres.")
    else:
        print("El numero ", num_tres, " es el numero mas grande de los tres.")
        

