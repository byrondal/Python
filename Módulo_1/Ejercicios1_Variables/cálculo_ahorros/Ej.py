nombre_usuario = input("Ingresa tu nombre")

print("Hola ", nombre_usuario)

dinero_hora = float(input("Cuánto ganas por hora?"))
horas_trabajo = float(input("Cuántas horas trabajas a la semana?"))

salario_semanal = dinero_hora * horas_trabajo
salario_anual = salario_semanal * 52

print(nombre_usuario, " tienes unas ganancias anuales de: ", salario_anual, " €")

gastos_semanales = float(input("A cuánto ascienden tus gastos semanales?"))

gastos_anuales = gastos_semanales * 52

ahorros_anuales = salario_anual - gastos_anuales

print(nombre_usuario, " estos son tus gastos anuales: ", gastos_anuales, " y estos serían tus ahorros anuales: ", ahorros_anuales)

trabajo_parcial_horas_semanales = 25
gastos_reducidos = gastos_anuales * 0.75

dinero_parcial_semanal = 25 * dinero_hora
dinero_parcial_anual = dinero_parcial_semanal * 52

ahorros_parciales = dinero_parcial_anual - gastos_reducidos

print("Estos serían tus gastos anuales con la reducción: ", gastos_reducidos, " € y estos serían tus ingresos nuevos: ", dinero_parcial_anual)
print("Estos serían tus ahorros con la nueva situación: ", ahorros_parciales, " €")

