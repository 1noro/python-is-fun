nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))
print("Hola", nombre)

if (edad >= 18) and (edad < 60):
    print("Eres un adulto. Te faltan", 60-edad, "años para ser un yayo.")
elif (edad < 18):
    print("Eres un joven. Te faltan", 18-edad, "años para ser un adulto.")
else:
    print("Eres un yayo. Te faltan", 100-edad, "años para morir.")

input("\nPulsa una tecla para salir...")
