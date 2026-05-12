def procesar_archivo(ruta):
    try:
        with open(ruta, 'r') as archivo:
            return archivo.read()
    except FileNotFoundError as e:
        print(f"Registrando error:{e}")
        raise  # Relanza la última excepción

def obtener_configuracion(archivo):
    try:
        with open(archivo, 'r') as f:
            return f.read()
    except FileNotFoundError as e:
        raise ConfigurationError(f"Archivo de configuración no encontrado:{archivo}") from e