#----Pedir al usuario que ingrese su tarjeta-----

num_tarjeta = input("Ingresa tu número de tarjeta ")

# 1234123412341234

print("**** **** **** ", num_tarjeta[12:16])

#----otra forma de resolverlo-----

longitud = len(num_tarjeta)
print("*" * (longitud-4) + num_tarjeta[longitud-4:longitud]) #podemos multiplicar strings por integers pero no por floats.







