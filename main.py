import unicodedata


def sanitizar(texto):
    """
    Limpia el texto ingresado por el usuario:
    - Convierte a minúsculas
    - Elimina tildes
    - Convierte ñ en n
    - Elimina diéresis
    """
    texto = texto.lower()
    texto = texto.replace("ñ", "n")

    texto_normalizado = unicodedata.normalize("NFD", texto)
    texto_limpio = ""

    for caracter in texto_normalizado:
        if unicodedata.category(caracter) != "Mn":
            texto_limpio += caracter

    return texto_limpio


def procesar_input(texto):
    """
    Identifica qué quiere hacer el usuario:
    - Si pregunta por clima o temperatura, regresa "clima"
    - Si pregunta por precio o acción, regresa "precio"
    - Si no reconoce la intención, regresa None
    """
    if "clima" in texto or "temperatura" in texto:
        return "clima"

    if "precio" in texto or "accion" in texto:
        return "precio"

    return None


print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")

user_input = sanitizar(input("---> "))

accion = procesar_input(user_input)

if accion == "clima":
    print("El usuario quiere consultar el clima.")

elif accion == "precio":
    print("El usuario quiere consultar el precio de una acción.")

else:
    print("No entendí tu solicitud.")
