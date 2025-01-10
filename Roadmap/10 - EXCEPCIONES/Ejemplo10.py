def division(x: float, y: float):
    return x / y

try:
    resultado = division(10, 0)
    print(resultado)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Fin del programa")

def contraseña(x: str):
    if len(x) < 10:
        raise ValueError("La contraseña debe tener más de 9 caracteres")

contraseña("123")


class Ortography(Exception):
    def __init__(self, text: str):
        self.text = text

def oracion(x: str):
    if x[-1] != ".":
        raise Ortography("El texto no termina en punto")
    if (x.isnumeric):
        raise Ortography("El texto no puede ser un número")
    if len(x) < 1:
        raise Ortography("El texto no puede estar vacío")