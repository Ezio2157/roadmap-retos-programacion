def contador(numero: int):
    if numero > 1:
        print(numero)
        contador(numero-1)
    else:
        print(numero)

def factorial(numero: int):
    if numero > 1:
        return numero * factorial(numero-1)
    else:
        return 1

def fibonacci(pos: int):
    if pos > 1:
        return pos + fibonacci(pos-1)
    elif pos == 1:
        return 1 + fibonacci(pos-1)
    elif pos == 0:
        return 0

contador(10)
print("--------------")
print("EL resultado factorial es: " + str(factorial(5)))
print("--------------")
print("EL resultado de fibonacci es: " + str(fibonacci(2)))