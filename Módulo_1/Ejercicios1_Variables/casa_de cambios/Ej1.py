#---pedir al usuario que ingrese la cantidad en euros---
euros = input("Ingresa la cantidad de euros que deseas convertir: ") #es tipo string

#---convertimos la cantidad ingresada a un float---
euros = float(euros)
#---convertir la cantidad de euros a dólares---
dolares = euros * 1.2

#---imprimir el resultado de la conversión---
print(euros, "euros son", dolares, "dólares")

