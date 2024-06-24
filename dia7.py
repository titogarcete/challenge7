import random
import string

# Función para generar una contraseña segura
def generar_contraseña(longitud):
    if longitud < 8 or longitud > 16:
        raise ValueError("La longitud debe estar entre 8 y 16 caracteres.")

    # Definir los caracteres permitidos
    caracteres = string.ascii_letters + string.digits + string.punctuation

    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    
    return contraseña

# Solicitar al usuario que ingrese la longitud de la contraseña
longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16 caracteres): "))

# Generar y mostrar la contraseña segura
try:
    contraseña_segura = generar_contraseña(longitud)
    print(f"Contraseña segura generada: {contraseña_segura}")
except ValueError as e:
    print(e)
