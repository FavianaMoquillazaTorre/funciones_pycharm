def retornar_promedio(v1, v2, v3):
    promedio = (v1 + v2 + v3) // 3
    return promedio



#Bloque principal
valor1 = int(input("Imgresar el primer valor: "))
valor2 = int(input("Ingresar el segundo valor: "))
valor3 = int(input("Ingresar el tercer valor: "))
print("Valor promedio de los tres numeros es: ")
print(retornar_promedio(valor1, valor2, valor3))