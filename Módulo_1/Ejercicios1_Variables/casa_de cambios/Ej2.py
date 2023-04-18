#---pedir al usuario que ingrese la cantidad en euros---
euros = input("Ingresa la cantidad de euros que deseas convertir: ") #es tipo string

#---convertimos la cantidad ingresada a un float---
euros = float(euros)
#---convertir la cantidad de euros a dólares---
dolares = euros * 1.2
#---calculamos lo que se queda la casa de cambios---
tasas_gestion = dolares *0.1

#---calculamos la cantidad de dólares que recibe el usuario---
dolares_recibidos = dolares - tasas_gestion

#---imprimimos el desglose de la operación---
print("Monto ingresado: ", euros, " euros")
print("Cambio en dólares: ", dolares, " dólares")
print("La Tasa de Gestión es: ", tasas_gestion, " dólares")
print("Monto recibido: ", dolares_recibidos, " dólares")
