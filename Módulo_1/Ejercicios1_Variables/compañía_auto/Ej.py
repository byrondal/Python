rbm_serie1_vendidos = int(input("Cuántos RBM Serie 1 has vendido? "))
rbm_serieplus_vendidos = int(input("Cuántos RBM Serie Plus has vendido?"))
rbm_todoterreno_vendidos = int(input("Cuántos RBM Todoterreno has vendido?"))


#-------guardamos los datos en variables---------

precio_rbmserie1 = 20000
precio_rbmserieplus = 35000
precio_rbmtodoterreno = 60000
comision_rbmserie1 = 0.03
comision_rbmserieplus = 0.05
comision_rbmtodoterreno = 0.07

#------calculamos la cantidad de euros a comisonar ese mes------


ganancia_rbm_serie1 = rbm_serie1_vendidos * precio_rbmserie1 * comision_rbmserie1
ganancia_rbm_serieplus = rbm_serieplus_vendidos * precio_rbmserieplus * comision_rbmserieplus
ganancia_rbm_todoterreno = rbm_todoterreno_vendidos * precio_rbmtodoterreno * comision_rbmtodoterreno

ganancia_general = ganancia_rbm_serie1 + ganancia_rbm_serieplus + ganancia_rbm_todoterreno

print("TU ganancia total para este mes es: ", ganancia_general, "€")