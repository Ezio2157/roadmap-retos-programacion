import os

def main():
    file_name = "Ezio2157.txt"

    ruta = "C:/Users/EZION/PycharmProjects/roadmap-retos-programacion/Roadmap/11 - MANEJO DE FICHEROS/Ezio2157.txt"

    contenido = ["\t-Aarón\n", "\t-21 años\n", "\t-Python\n"]

    if not os.path.exists(ruta):
        with open(file_name,"w") as file:
            file.writelines(contenido)

    with open(file_name, "r") as file:
        print(file.read())

    if os.path.exists(ruta):
        os.remove(ruta)

def ejemplo():
    FILE = "Ventas.txt"
    RUTA = "C:/Users/EZION/PycharmProjects/roadmap-retos-programacion/Roadmap/11 - MANEJO DE FICHEROS/Ventas.txt"

    flag = True

    while flag:

        print(f"""---------------------------
            
            1. Nueva Venta
            2. Consultar Venta
            3. Actualizar Venta
            4. Borrar Venta
            5. Mostrar Ventas
            6. Venta total
            7. Venta total por producto
            8. Salir
        """)
        option = int(input("\nSelecciona una opcion: "))

        match option:
            case 1:
                print("---------------------------")
                nombre = input("Introduce el nombre del producto: ")
                cantidad = input("Introduce la cantidad vendida del producto: ")
                precio = input("Introduce el precio del producto: ")
                with open(FILE, "a") as file:
                    file.write(f"{nombre},{cantidad},{precio}\n")
                    print("Venta añadida con éxito.")

            case 2:
                print("---------------------------")
                nombre = input("Introduce el nombre del producto: ")
                with open(FILE, "r") as file:
                    for venta in file:
                        if nombre == venta.split(",")[0]:
                            print(venta)
                            break

            case 3:
                print("---------------------------")
                nombre = input("Introduce el nombre del producto: ")
                cantidad = input("Introduce la cantidad vendida del producto: ")
                precio = input("Introduce el precio del producto: ")
                with open(FILE, "r") as file:
                    ventas = file.readlines()
                with open(FILE, "w") as file:
                    for venta in ventas:
                        if nombre != venta.split(",")[0]:
                            file.write(venta)
                        else:
                            file.write(f"{nombre},{cantidad},{precio}\n")
                    print("Venta actualizada con éxito.")

            case 4:
                print("---------------------------")
                nombre = input("Introduce el nombre del producto: ")
                with open(FILE, "r") as file:
                    ventas = file.readlines()
                with open(FILE, "w") as file:
                    for venta in ventas:
                        if nombre != venta.split(",")[0]:
                            file.write(venta)
                    print("Venta eliminada con éxito.")

            case 5:
                print("---------------------------")
                with open(FILE, "r") as file:
                    for venta in file:
                        venta_list = venta.split(",")
                        print(f"{venta_list[1]} {venta_list[0]} vendidos a {venta_list[2]} (Total = {int(venta_list[1]) * float(venta_list[2])})")

            case 6:
                print("---------------------------")
                total = 0
                with open(FILE, "r") as file:
                    for venta in file:
                        cantidad = int(venta.split(",")[1])
                        precio = float(venta.split(",")[2])
                        total += cantidad * precio
                print(f"La venta total es de: {total}")

            case 7:
                print("---------------------------")
                nombre = input("Introduce el nombre del producto: ")
                total = 0
                with open(FILE, "r") as file:
                    for venta in file:
                        if nombre == venta.split(",")[0]:
                            cantidad = int(venta.split(",")[1])
                            precio = float(venta.split(",")[2])
                            total += cantidad * precio
                print(f"La venta total de {nombre} es de: {total}")

            case 8:
                flag = False
                if os.path.exists(RUTA):
                    os.remove(RUTA)

if __name__ == "__main__":
    #main()
    ejemplo()