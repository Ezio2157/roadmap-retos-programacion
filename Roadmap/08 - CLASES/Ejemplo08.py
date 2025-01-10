class Pila:
    def __init__(self):
        self.datos = []

    def añadir(self, item):
        self.datos.append(item)

    def borrar(self):
        if len(self.datos) != 0:
            return self.datos.pop(len(self.datos)-1)
        else:
            print("No hay contenido en la Pila")

    def mostrar_contenido(self):
        print("--------Pila---------")
        for item in self.datos:
            print(item)
        print("---------------------")

class Cola:
    def __init__(self):
        self.datos = []

    def añadir(self, item):
        self.datos.append(item)

    def borrar(self):
        if len(self.datos) != 0:
            return self.datos.pop(0)
        else:
            print("No hay contenido en la lista")

    def mostrar_contenido(self):
        print("--------Cola---------")
        for item in self.datos:
            print(item)
        print("---------------------")

stack = Pila()
queue = Cola()

stack.añadir(1)
stack.añadir(2)
stack.añadir(3)
stack.añadir(4)

queue.añadir(1)
queue.añadir(2)
queue.añadir(3)
queue.añadir(4)

stack.borrar()
queue.borrar()

stack.mostrar_contenido()
queue.mostrar_contenido()