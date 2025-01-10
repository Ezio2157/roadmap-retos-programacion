#Función simple

def Funcion_Test():
    var = 1
    var2 = "Funcion sin funcionalidad"
    print(var2)

Funcion_Test()

#Funcion con retorno

def Funcion_Retorno(num1, num2):
    return num1 * num2

print(Funcion_Retorno(2,3))


string = "Cadena de texto de ejemplo"

print("LA cadena de texto definida tiene una longitud de", len(string))

print("---------------------------------")


def Funcion_Extra(cad1, cad2):
    count = 0
    for i in range(1,101):
        if(i%3 == 0) and (i%5 == 0):
            print(cad1+cad2)
        elif i%3 == 0:
            print(cad1)
        elif i%5 == 0:
            print(cad2)
        else:
            print(i)
            count += 1
    print("-----------------------")
    return count

print(f"Se han imprimido un total de {Funcion_Extra("Fizz","Buzz")} números")


print("---------------------------")

#Lambdas

suma = lambda a,b : a+b

print(f"La suma de 2 y 3 es igual a {suma(2,3)}")
