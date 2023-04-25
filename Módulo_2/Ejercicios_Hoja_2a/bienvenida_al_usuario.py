user = input("Introduce tu nombre: ")


if user.lower() != ("alejandro" or "naomi" or "sergio"):
  if user.find("#" or ".") >= 0:
    print("Porfavor, introduzca su nombre sin caracteres especiales! ")
    user = input("Vuelva a introducir su nombre porfavor: ")
    if user.lower() != ("alejandro" or "naomi" or "sergio"):
      print("Bienvenido ", user.title(), "!")
  else:
    print("Bienvenido Invitado!")
else:
  print("Bienvenido ", user.title(), "!")






