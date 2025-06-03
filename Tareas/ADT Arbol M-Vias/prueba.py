from ArbolMVias import ArbolMVias


if __name__ == "__main__":
    # Creamos un árbolMVias de orden 3
    arbol = ArbolMVias(3)

    # Insertamos algunas claves
    claves = [10, 20, 5, 15, 30, 25]
    for clave in claves:
        arbol.insertar(clave)

    # Visualizamos el arbol
    print(arbol.visualizar())

    # Realizamos recorridos
    print("Inorden:", arbol.recorrido_inorden())   
    print("Preorden:", arbol.recorrido_preorden()) 
    print("Postorden:", arbol.recorrido_postorden()) 

    # Buscamos claves
    print("Existe 15?:", arbol.buscar(15))  
    print("Existe 40?:", arbol.buscar(40))  