
def suma(a,b):
    try:
        resultado = a + b
    except TypeError:
        print("Error: Tipo de dato no válido.")
    else:
        return resultado

def resta(a,b):
    try:
        resultado = a - b
    except TypeError:
        print("Error: Tipo de dato no válido.")
    else:
        return resultado

def producto(a,b):
    try:
        resultado = a * b
    except TypeError:
        print("Error: Tipo de dato no válido.")
    else:
        return resultado

def division(a,b):
    try:
        resultado = a / b
    except TypeError:
        print("Error: Tipo de dato no válido.")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    else:
        return resultado