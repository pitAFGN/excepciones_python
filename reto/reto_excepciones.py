def dividir_numeros():
    try:
        # Solicitar al usuario que introduzca dos números
        entrada1 = input("Introduce el primer número: ")
        entrada2 = input("Introduce el segundo número: ")
        
        # Convertir las entradas a números enteros
        num1 = int(entrada1)
        num2 = int(entrada2)
        
        # Realizar la división del primer número entre el segundo
        resultado = num1 / num2
        
        # Devolver el resultado de la división
        return resultado
    
    except ValueError:
        # Si el usuario introduce algo que no se puede convertir a entero
        print("Error: Debes introducir un número válido")
    
    except ZeroDivisionError:
        # Si el usuario intenta dividir entre cero
        print("Error: No es posible dividir entre cero")
    
    finally:
        # Se ejecuta independientemente de si hubo éxito o error
        print("Operación finalizada")

# Llamada a la función
resultado_final = dividir_numeros()

# Mostrar el resultado solo si la operación fue exitosa
if resultado_final is not None:
    print(f"El resultado de la división es: {resultado_final}")