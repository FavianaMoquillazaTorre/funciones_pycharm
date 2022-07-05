def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

print("//// Primer Rectangulo ////")
lado1 = int(input("Ingresar el valor de la base: "))
lado2 = int(input("Ingresar el valor de la altura: "))
print("La superficie del primer rectangulo es: ")
print(retornar_superficie(lado1, lado2))
print("*******************************")
def retornar_superficie(lado3, lado4):
    superficie = lado3 * lado4
    return superficie
print("//// Segundo Rectangulo ////")
lado3 = int(input("Ingresar el valor de la base: "))
lado4 = int(input("Ingresar el valor de la altura: "))
print("La superficie del segundo rectangulo es: ")
print(retornar_superficie(lado3, lado3))
print("*******************************")
if retornar_superficie(lado1, lado2) > retornar_superficie(lado3, lado4):
    print("La superficie del primer rectangulo es mayor")
else:
    print("La superficie del segundo rectangulo es mayor")
