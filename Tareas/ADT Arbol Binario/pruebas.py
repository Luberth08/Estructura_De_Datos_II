'''
    Title: Un programa que prueba la clase Nodo y la clase ArbolBinario
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 02/04/2025
    Version: 1.0 
'''


# Importamos las clases necesarias para la prueba
from Nodo import Node
from Arbol_Binario import BinaryTree


def main():
    '''
        Función principal que prueba las funciones de la clase ArbolBinario.
        
        Parameters:
            None
        Returns:
            None
    '''
    # Creamos un árbol binario
    arbol = BinaryTree()
    
    # Insertamos nodos en el árbol
    arbol.insertar_nodo(7)
    arbol.insertar_nodo(5)
    arbol.insertar_nodo(2)
    arbol.insertar_nodo(3)
    arbol.insertar_nodo(6)
    arbol.insertar_nodo(9)
    arbol.insertar_nodo(8)
    arbol.insertar_nodo(12)
    arbol.insertar_nodo(10)

    # Imprimimos el árbol en inorden
    print("Árbol en inorden:")
    print(arbol.inorden())
    print("\n") # Salto de línea para separar la salida

    # Imprimimos el árbol en preorden
    print("Árbol en preorden:")
    print(arbol.preorden())
    print("\n") # Salto de línea para separar la salida

    # Imprimimos el árbol en postorden
    print("Árbol en postorden:")
    print(arbol.postorden())

    # Imprimimos la altura del nivel del árbol
    print("\nAltura del árbol:" + str(arbol.altura()))

    # Imprimimos el ancho del árbol
    print("\nAncho del árbol:" + str(arbol.hojas()))

    # Imprimimos el número de nodos del árbol
    print("\nNúmero de nodos del árbol:" + str(arbol.cantidad()))

    # Imprimimos el arbol en dfs
    print("\nRecorrido en dfs del árbol:")
    print(arbol.dfs())

    # Imprimimos el arbol en bfs
    print("\nRecorrido en bfs del árbol:")
    print(arbol.bfs())

    # Dibujamos el arbol en consola
    print("\nDibujo del árbol: \n")
    arbol.dibujar()

    # Eliminamos un nodo con dos hijos
    arbol.eliminar_nodo(5)

    # Dibujamos el arbol en consola después de eliminar el nodo
    print("\nDibujo del árbol después de eliminar el nodo 9: \n")
    arbol.dibujar()


if __name__ == "__main__":
    # Llamamos a la función principal para ejecutar el programa
    main()
