def cantidad_letra_a(palabra):
    cantidad = 0
    for i in range(len(palabra)):
        if (palabra [i] == "a") or (palabra[i] == "A"):
            cantidad += 1
    return cantidad

palabra = input("Ingresar una palabra: ")
print("La palabra", palabra, "tiene", cantidad_letra_a(palabra), "a")