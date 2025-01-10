class Animal:

    def __init__(self,nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"Hola, {self.sonido}")

class Perro(Animal):

    def __init__(self,nombre,sonido,raza):
        super().__init__(nombre,sonido)
        self.raza = raza

    def saludar(self):
        print(f"Soy un perro de raza {self.raza} y mi nombre es {self.nombre}")

class Gato(Animal):

    def __init__(self,nombre,sonido,pelaje):
        super().__init__(nombre,sonido)
        self.pelaje = pelaje

    def saludar(self):
        print(f"Soy un gato de pelaje {self.pelaje} y mi nombre es {self.nombre}")

roque = Perro("Roque","Guau","Labrador")
oreo = Gato("Oreo", "Miau", "Blanco")

roque.saludar()
oreo.saludar()

"""-----------------------------------------"""

class Empleado:

    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre

class Gerente(Empleado):

    def __init__(self,id,nombre,cargo_ejecutivo):
        super().__init__(id,nombre)
        self.cargo_ejercutivo = cargo_ejecutivo
        self.empleados_a_cargo = []

    def subirse_sueldo(self):
        print("Me subo el sueldo!!!!")

    def add_empleados(self,empleado:Empleado):
        self.empleados_a_cargo.append(empleado)

class Gerente_de_proyectos(Empleado):

    def __init__(self,id,nombre,nombre_proyecto):
        super().__init__(id,nombre)
        self.nombre_proyecto = nombre_proyecto
        self.empleados_a_cargo = []

    def acelerar_proyecto(self):
        print("Vamos tarde!!!!")

class Programador(Empleado):

    def __init__(self,id,nombre,lenguaje_favorito):
        super().__init__(id,nombre)
        self.lenguaje_favorito = lenguaje_favorito

    def soltar_facto(self):
        print("Si fuera queriiiooo...")

Paco = Gerente("1","Paco","CEO")
Pepe = Gerente_de_proyectos("2","Pepe","IA")
Kiko = Gerente_de_proyectos("7","Kiko","App de escritorio")
Jose = Programador("3","Jose","Python")
Luis = Programador("4","Luis","C++")
Antonio = Programador("5","Antonio","Java")
Miguel = Programador("6","Miguel","Python")

Paco.add_empleados(Pepe)
Paco.add_empleados(Kiko)