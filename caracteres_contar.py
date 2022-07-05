def largo(cadena):
    return len(cadena)

#Bloque principal del programa
nombre1 = input("Ingresar el primer nombre: ")
nombre2 = input("Ingresar el segundo nombre: ")
la1 = largo(nombre1)
la2 = largo(nombre2)
if la1 == la2:
    print("Los nombres:", nombre2, "y", nombre2, "Tienen la misma cantidad de caracteres.")
else:
    if la1 > la2:
        print(nombre1, "Es el mas largo")
    else: 
        print(nombre2, "Es el mas largo")