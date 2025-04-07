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
    arbol.insertar_nodo(50)
    arbol.insertar_nodo(48)
    arbol.insertar_nodo(36)
    arbol.insertar_nodo(25)
    arbol.insertar_nodo(37)
    arbol.insertar_nodo(49)
    arbol.insertar_nodo(67)
    arbol.insertar_nodo(65)
    arbol.insertar_nodo(87)
    arbol.insertar_nodo(90)

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

    # Eliminamos valores del árbol
    arbol.eliminar(49)  
    arbol.eliminar(87) 
    arbol.eliminar(50) 

    # Dibujamos el arbol en consola
    print("\nDibujo del árbol: \n")
    arbol.dibujar()


if __name__ == "__main__":
    # Llamamos a la función principal para ejecutar el programa
    main()
