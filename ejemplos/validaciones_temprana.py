def procesar_datos(datos):
    # Validación al inicio
    if datos is None:
        raise ValueError("Los datos no pueden ser None")
    if not isinstance(datos, list):
        raise TypeError("Los datos deben ser una lista")
    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacía")

    # Procesamiento principal
    resultado = []
    for item in datos: