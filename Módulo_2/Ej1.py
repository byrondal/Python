#---Crea un script que dado un usuario le de una bienvenida personalizada si es el administrador
#---y una bienvenida genérica si es otra persona

#---Pedir al usuario que introduzca su nombre----
nombre = input("Introduce tu nombre")
administrador = "alejandro"

#----Comprobar si ese nombre es igual que el del administrador----

if nombre.lower() == administrador:
    print("Bienvenido, ", nombre, "!")
else:
    print("Bienvenido invitado!")
