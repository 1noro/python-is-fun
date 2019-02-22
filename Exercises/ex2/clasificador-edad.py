nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
print("Hola", nombre)

if (edad >= 18) and (edad < 60):
    print("Eres un adulto.")
elif (edad < 18):
    print("Eres un joven.")
else:
    print("Eres un yayo.")

input("\nPulsa una tecla para salir...")
