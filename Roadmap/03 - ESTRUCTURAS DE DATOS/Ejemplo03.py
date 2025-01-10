#En python existen 4 estructuras de datos primitivas, listas, tuplas, diccionarios y conjuntos

def mostrar(estruct):
    print("--------------")
    for i in estruct:
        print(i)

def mostrar_dicc(datos):
    print("---------------")
    for clave in datos:
        print(f"Clave: {clave} || Valor: {datos[clave]}")

#Listas

lista = [1, 2, 3, 4, "uno", 2.4, 5j, "uno", "uno", 9]

lista.remove(1)
print(f"El elemento borrado con indice 2 de la lista es {lista.pop(2)}")
print(f"El número de veces que aparece 'uno' en la lista es {lista.count("uno")}")
lista.insert(0,1)
mostrar(lista)
lista_copia = lista.copy()
lista.remove(2.4)
mostrar(lista)
mostrar(lista_copia)
lista_copia.clear()
mostrar(lista_copia)
mostrar(lista)


#Tuplas

tupla = (1,1,2,3,4,5,6,"uno","dos","tres")

mostrar(tupla)
print("------------")
print(f"La cantidad de veces que aparece el número 1 es {tupla.count(1)}")


#Diccionarios

dicc = {"dato1":1, "dato2":2, "dato3":"tres", "dato4":4}

print(f"El valor de la clave 'dato1' es {dicc.get("dato1")}")

dicc.update({"dato1":5})

print(f"El valor de la clave 'dato2' es {dicc.get("dato2")}")

print(f"El valor que tienen las claves 'dato1' y 'dato2' son {dicc.fromkeys(["dato1", "dato2"], "test")}")

mostrar_dicc(dicc)

#Conjuntos


