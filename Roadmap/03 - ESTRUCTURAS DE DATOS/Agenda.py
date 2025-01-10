def buscar_contacto(nombre, datos):
    contacto = datos.get(nombre)
    if contacto == None:
        print("No hay registros con ese nombre")
    else:
        print(f"Nombre: {nombre} || Número de teléfono: {contacto}\n")

def insertar_contacto(nombre,numero,datos):
    if len(numero) < 12 and numero.isnumeric():
        datos[nombre] = numero
        print("Nuevo usuario insertado con éxito\n")
    else:
        print("ERROR. Formato incorrecto de número\n")

def actualizar_contacto(nombre,numero,datos):
    if len(numero) < 12 and numero.isnumeric():
        datos[nombre] = numero
        print("Contacto modificado con éxito\n")
    else:
        print("ERROR. Formato incorrecto de número\n")

def eliminar_contacto(nombre, datos):
    datos.pop(nombre)
    print("Contacto borrado con éxito\n")

def mostrar_contactos(datos):
    print("---------------")
    for clave in datos:
        print(f"Nombre: {clave} || Número de teléfono: {datos[clave]}")
    print("---------------\n")

flag = True
datos = {"Pepe":927929210}

while flag:
    print(f"""Bienvenido a la agenda virtual
        1) Buscar Contacto
        2) Insertar Contacto
        3) Actualizar Contacto
        4) Eliminar Contacto
        5) Mostrar contactos
        6) Salir
    """)
    option = input("\nSeleccione una opción:")

    if option == '1':
        nombre = input("\nIntroduce el nombre que quieres buscar: ")
        buscar_contacto(nombre,datos)
    elif option == '2':
        nombre = input("\nIntroduce el nombre del nuevo contacto: ")
        numero = input("Introduce el número del nuevo contacto: ")
        insertar_contacto(nombre, numero, datos)
    elif option == '3':
        nombre = input("\nIntroduce el nombre del contacto: ")
        numero = input("Introduce el número nuevo del contacto: ")
        actualizar_contacto(nombre,numero,datos)
    elif option == '4':
        nombre = input("\nIntroduce el nombre del contacto que deseas borrar: ")
        eliminar_contacto(nombre,datos)
    elif option == '5':
        mostrar_contactos(datos)
    elif option == '6':
        flag = False
        print("Hasta pronto")
    else:
        print("Opción no válida")