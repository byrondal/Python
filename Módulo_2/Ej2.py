''' Pide un número por pantalla e indica si el número es un
múltiplo de 3 (en el sentido de que la división de como
resultado un número entero '''

#---Pedir número entero----

numero = input("Introduce un numero entero: ")
numero = int(numero)

#----comprobar que el número se un múltiplo de 3----

if numero % 3 == 0:
    print("Este número es un múltiplo de 3")
else:
    print("Este número no es múltiplo de 3")

