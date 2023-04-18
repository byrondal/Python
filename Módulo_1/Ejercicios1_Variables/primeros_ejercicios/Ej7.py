print("Cómo te llamas?")
nombre = input()
lenguaje = "python"
nombre = nombre.replace(".", "")
mensaje = "Hola!, " + nombre.title() + ", estás usando " + lenguaje.title() + "!"
print(mensaje)