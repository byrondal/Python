precio_ensalada_mixta = 12
precio_sopa_pescado = 10
dorada_horno = 18
arroz_curry = 14
lasaña_carne = 15
brownie = 8
helado = 6
refrescos = 5.5
cafe = 3.5

#-----Pedir al usuario que introduzca la cantidad de cada alimento que ha consumido------

cantidad_ensalada_mixta = int(input("Cuántas ensaladas mixtas se han consumido? "))
cantidad_sopa_pescado = int(input("Cuántas sopas de pescado se han consumido?"))
cantidad_dorada_horno = int(input("Cuántas doradas al horno se han consumido?"))
cantidad_arroz_curry = int(input("Cuántos arroces al curry se han consumido?"))
cantidad_lasaña_carne = int(input("Cuántas lasañas de carne se han consumido?"))
cantidad_brownie_carne = int(input("Cuántos brownies de chocolate se han consumido?"))
cantidad_helado = int(input("Cuántos helados se han consumido?"))
cantidad_refresco = int(input("Cuántos refrescos se han consumido?"))
cantidad_cafe = int(input("Cuántos cafés se han consumido?"))

#----Calculamos el total de la cuenta-------

total = cantidad_ensalada_mixta * precio_ensalada_mixta + cantidad_sopa_pescado * precio_sopa_pescado + cantidad_dorada_horno * dorada_horno + cantidad_arroz_curry * arroz_curry 