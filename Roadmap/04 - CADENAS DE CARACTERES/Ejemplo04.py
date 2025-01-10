def es_palindromo():
    if palabra is not None and palabra2 is not None:
        if palabra2 == palabra[::-1]:
            print(palabra + " y " + palabra2 + " son Palíndromos")
        else:
            print(palabra + " y " + palabra2 + " no son Palíndromos")
    else:
        print("Debe elegir primero las palabras a analizar")

def es_anagrama():
    son = True
    if palabra is not None and palabra2 is not None:
          if len(palabra) == len(palabra2):
              for letra in palabra[0:len(palabra)]:
                  if letra not in palabra2:
                      son = False
                      break
          else:
              son = False
          if son:
              print(palabra + " y " + palabra2 + " son Anagramas")
          else:
              print(palabra + " y " + palabra2 + " no son Anagramas")
    else:
        print("Debe elegir primero las palabras a analizar")

def es_isograma():
    son = True
    if palabra is not None and palabra2 is not None:
        if len(palabra) == len(palabra2):
            for letra in palabra[0:len(palabra)]:
                if palabra.count(letra) != palabra2.count(letra):
                    son = False
                    break
        else:
            son = False
        if son:
            print(palabra + " y " + palabra2 + " son Isogramas")
        else:
            print(palabra + " y " + palabra2 + " no son Isogramas")
    else:
        print("Debe elegir primero las palabras a analizar")


flag = True
palabra = None
palabra2 = None

while flag:
    print(f"""
        1)  Analisis de Palíndromo
        2)  Analisis de Anagrama
        3)  Analisis de Isograma 
        4)  Todos los Analisis
        5)  Elegir palabras (actualmente --> Palabra1 = {palabra} || Palabra2 = {palabra2})
        6)  Salir
    """)

    option = int(input("\nIntroduzca la opción deseada: "))
    if option == 1:
        es_palindromo()
    elif option == 2:
        es_anagrama()
    elif option == 3:
        es_isograma()
    elif option == 4:
        es_palindromo()
        es_anagrama()
        es_isograma()
    elif option == 5:
        palabra = input("Introduce la primera palabra que se desea analizar: ")
        palabra2 = input("Introduce la segunda palabra que se desea analizar: ")
    elif option == 6:
        flag = False
    else:
        print("Opción no válida")