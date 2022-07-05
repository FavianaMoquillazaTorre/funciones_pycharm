def retornar_mayor(v1, v2):
    if v1 > v2:
        mayor = v1
    else:
        mayor = v2
    return mayor

# Bloque principal
valor1 = int(input("Ingresar el primer valor: "))
valor2 = int(input("Ingresar el segundo valor: "))
print("El numero mayor es: ", retornar_mayor(valor1, valor2))