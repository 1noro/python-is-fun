nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
print("Hola", nombre)

if (edad >= 18) and (edad < 60):
    print("Eres un adulto.")
elif (edad >= 0) and (edad < 18):
    print("Eres un joven.")
elif (edad >= 60):
    print("Eres un yayo.")
else:
    print("No puedes tener una edad negativa.")

input("\nPulsa una tecla para salir...")
