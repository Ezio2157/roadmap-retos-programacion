from click import option

flag = True
index = 0
option = 0
paginas = []

while flag:
    if len(paginas) != 0:
        print("\nPagina actual " + paginas[index] + " (" + str(index) + ")")
    else:
        print("\nNo hay páginas")

    option = input("\n1)\tAgregar una nueva url\n2)\tIr adelante\n3)\tIr hacia atrás\n4)\tSalir\n\nSeleccione una opción: ")

    match option:
        case "1":
            url = input("\nIntroduce la nueva web: ")
            paginas.append(url)
            if len(paginas) > 1:
                index += 1
        case "2":
            if index+1 == len(paginas):
                print("\nEstas en la página mas reciente")
            else:
                index += 1
                print("\nAhora estas en la página '" + paginas[index] + "'")
        case "3":
            if index == 0:
                print("\nEstas en la página mas antigua")
            else:
                index -= 1
                print("\nAhora estas en la página '" + paginas[index] + "'")
        case "4":
            flag = False

    print("---------------------")