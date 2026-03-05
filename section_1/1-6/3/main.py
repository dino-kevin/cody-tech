print("Ingrese la edad para su sim de telcel, porfis")

age = int(input())

if age >= 18:
    print("El usuario puede generar su nuevo sim")
    print(f'La edad de la persona que quiere el sim es de: {age}')

else:
    print("Necesitas de una persona responsable de ti para poder darte el sim")
    exit



