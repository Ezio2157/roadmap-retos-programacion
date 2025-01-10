#Operaciones aritmeticas
from markdown_it.common.utils import escapeHtml

a = 2
b = 2

print("La suma de A y B es", a+b)
print("La resta es", a-b)
print("La multiplicación es", a*b)
print("La división es", a/b)
print("El módulo es", a%b)
print("La division entera es", a//b)
print("La exponenciación es", a**b)

print("----------------------------------------------")

#Operaciones lógicas

a = True
b = False

print("La relacion AND es", a and b)
print("La relación OR es", a or b)
print("La negacion NOT de B es", not b)

print("----------------------------------------------")

#Operaciones de comparación

a = 2
b = 3

print(f"""Las operaciones de comparación son
    Mayor que: {a>b}
    Menor que: {a<b}
    Mayor o igual: {a>=b}
    Menor o igual: {a<=b}
    Igual: {a==b}
    Distinto: {a!=b}
""")

print("----------------------------------------------")

#Operaciones de asignación

a += b
print("Incremento B en A:", a)

a -= b
print("Decremento B en A:", a)

a *= b
print("Incremento multiplicativo B en A:", a)

print("----------------------------------------------")

#Operaciones de identidad

es = a is b
no_es = a is not b

print(f"""    Es: {es}
    NO es: {no_es}
""")

print("----------------------------------------------")

#Operaciones de pertenencia

a = "Drako"
b = "Kuki"

en =  a in b
no_en = a not in b

print(f"""Las operaciones de pertenencia son
    En: {en}
    NO en:{no_en}
""")

print("----------------------------------------------")

#Operaciones a nivel de bits

a = 1
b = 2

print(f"""Las operaciones a nivel de bits son
    Bits AND: {a&b}
    Bits OR: {a|b}
    Bits NOT: {~a}
    Bits XOR: {a^b}
""")

print("----------------------------------------------")

#Estructuras de control

if a > b:
    print("A es mayor que B")
elif a < b:
    print("A es menor que B")
else:
    print("A y B son iguales")

print("----------------------------------------------")

for i in range(0,5):
    print(f"Iteracion (for) {i}")

j=0

while j < 5:
    print(f"Iteracion (while) {j}")
    j+=1

print("----------------------------------------------")

#Ejercicio Extra

for i in range(10,56):
    if (i%2 == 0) and (i != 16) and (i%3 != 0):
        print(i)