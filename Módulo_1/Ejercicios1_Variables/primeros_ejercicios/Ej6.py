print("Cómo te llamas?")
nombre = input()
nombre = nombre.replace(".", "")
mensaje = "Hola!, " + nombre.title() + ", estás usando python"
print(mensaje)