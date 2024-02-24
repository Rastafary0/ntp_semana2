numero = input("Introduce un número: ")

try:
    numero = int(numero)
    if numero > 0:
        print("El número es positivo")
    else:
        print("El número es negativo")
except ValueError:
    print("El número introducido no es válido")
