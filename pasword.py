password = input("Ingresa tu contraseña: ")

if len(password) < 8:
    print("Tu contraseña debe tener al menos 8 caracteres.")

elif password.islower():
    print("Tu contraseña debe contener al menos una letra mayúscula.")

elif password.isalpha():
    print("Tu contraseña debe contener al menos un número.")
else:
    print("Tu contraseña es segura :)")