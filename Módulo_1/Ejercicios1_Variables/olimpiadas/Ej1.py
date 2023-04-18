#---Pedimos los tiempos por pantalla---

tiempo_hannah = input("Ingresa el tiempo de Hannah Neise (formato: minutos segundos centésimas): ")
tiempo_jackie = input("Ingresa el tiempo de Jackie Narracott (formato: minutos segundos centésimas): ")
tiempo_kimberly = input("Ingresa el tiempo de Kimberly Bos (formato: minutos segundos centésimas): ")

#-----Extraer minutos segunod y centésimas-----

minutos_hannah, segundo_hannah, centesimas_hannah = tiempo_hannah.split(" ")
minutos_jackie, segundo_jackie, centesimas_jackie = tiempo_jackie.split(" ")
minutos_kimberly, segundo_kimberly, centesimas_kimberly = tiempo_kimberly.split(" ")

#-----Convertimos los tiempos a segundos----

tiempo_hannah = float(minutos_hannah) * 60 + float(segundo_hannah) + float(centesimas_hannah) *0.01
tiempo_jackie = float(minutos_jackie) * 60 + float(segundo_jackie) + float(centesimas_jackie) *0.01
tiempo_kimberly = float(minutos_kimberly) * 60 + float(segundo_kimberly) + float(centesimas_kimberly) *0.01

#----Calculamos al velocidad media --------

velocidad_hannah = 100/tiempo_hannah
velocidad_jackie = 100/tiempo_jackie
velocidad_kimberly = 100/tiempo_kimberly

#------Imprimier los resutlados por pantalla------

print("La velocidad media de Hannah Neise fue de: ", velocidad_hannah, " metros por segundo")
print("La velocidad media de Jackie Narracott fue de: ", velocidad_jackie, " metros por segundo")
print("La velocidad media de Kimberly Bos fue de: ", velocidad_kimberly, " metros por segundo")
