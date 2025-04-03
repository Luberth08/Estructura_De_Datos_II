'''
    Title: Una clase que implementa los atributos y metodos de un Arbol Binario
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 01/04/2025
    Version: 1.0 
'''

# Importamos la clase Node desde el archivo Nodo.py
from Nodo import Node


# Definimos la clase ArbolBinario
class BinaryTree:   
    '''
        Clase que simula el comportamiento de un árbol binario

        Attributes:
            raiz (Nodo): Nodo raíz del árbol.
    '''

    def __init__(self):
        '''
            Metodo constructor de la clase
        '''
        # Definimos la variable privada de la clase
        self.__raiz = None

    # Método Getter y Setter para 'raiz'
    def get_raiz(self):
        '''Devuelve el nodo raiz del arbol'''
        return self.__raiz

    def set_raiz(self, raiz: Node):
        '''Establece el nodo raiz del arbol'''
        self.__raiz = raiz

    # Metodo para representar el arbol en string
    def __str__(self):
        '''Devuelve una representación en string del árbol binario'''
        return "Arbol Binario con raiz: " + str(self.__raiz)

    # Método para insertar un nuevo nodo en el árbol binario
    def insertar(self, valor: int):
        '''
            Inserta un nuevo nodo en el árbol binario.

            Parameters:
                valor (int): Valor del nuevo nodo.
        '''
        nuevo_nodo = Node(valor)

        # Verificamos si el árbol está vacío
        # Si no esta vacio, llamamos al método privado para insertar el nuevo nodo en el lugar correcto
        if self.__raiz is None:
            self.__raiz = nuevo_nodo
        else:
            self.__insertar_recursivo(self.__raiz, nuevo_nodo)

    # Método privado para insertar un nuevo nodo de forma recursiva
    def __insertar_recursivo(self, nodo_actual: Node, nuevo_nodo: Node):
        '''
            Método privado que inserta un nuevo nodo en el árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
                nuevo_nodo (Node): Nodo a insertar.
        '''
        # Comparamos el valor del nuevo nodo con el nodo actual
        if nuevo_nodo.get_valor() < nodo_actual.get_valor():
            # Si el nodo izquierdo es None, insertamos el nuevo nodo
            # Si no, seguimos buscando en el subárbol izquierdo
            if nodo_actual.get_izquierda() is None:
                nodo_actual.set_izquierda(nuevo_nodo)
            else:
                self.__insertar_recursivo(nodo_actual.get_izquierda(), nuevo_nodo)
        else:
            # Si el nodo derecho es None, insertamos el nuevo nodo
            # Si no, seguimos buscando en el subárbol derecho
            if nodo_actual.get_derecha() is None:
                nodo_actual.set_derecha(nuevo_nodo)
            else:
                self.__insertar_recursivo(nodo_actual.get_derecha(), nuevo_nodo)
    
    # Método para eliminar un nodo del árbol binario
    def eliminar(self, valor: int):
        '''
            Elimina un nodo del árbol binario.

            Parameters:
                valor (int): Valor del nodo a eliminar.
        '''
        self.__raiz = self.__eliminar_recursivo(self.__raiz, valor)

    # Método privado para eliminar un nodo de forma recursiva
    def __eliminar_recursivo(self, nodo_actual: Node, valor: int):
        '''
            Método privado que elimina un nodo en el árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
                valor (int): Valor del nodo a eliminar.
            Returns:
                Node: Nodo actualizado después de la eliminación.
        '''
        # Verificamos si el nodo actual es None
        if nodo_actual is None:
            return nodo_actual

        # Comparamos el valor del nodo actual con el valor a eliminar
        if valor < nodo_actual.get_valor():
            nodo_actual.set_izquierda(self.__eliminar_recursivo(nodo_actual.get_izquierda(), valor))
        elif valor > nodo_actual.get_valor():
            nodo_actual.set_derecha(self.__eliminar_recursivo(nodo_actual.get_derecha(), valor))
        else:
            # Nodo encontrado, eliminamos el nodo
            if nodo_actual.get_izquierda() is None:
                return nodo_actual.get_derecha()
            elif nodo_actual.get_derecha() is None:
                return nodo_actual.get_izquierda()

            # Nodo con dos hijos, encontramos el sucesor inorden (mínimo en el subárbol derecho)
            temp = self.__minimo(nodo_actual.get_derecha())
            nodo_actual.set_valor(temp.get_valor())
            nodo_actual.set_derecha(self.__eliminar_recursivo(nodo_actual.get_derecha(), temp.get_valor()))

        return nodo_actual  

    # Método privado para encontrar el nodo con el valor mínimo en un subárbol
    def __minimo(self, nodo_actual: Node):
        '''
            Método privado que encuentra el nodo con el valor mínimo en un subárbol.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                Node: Nodo con el valor mínimo.
        '''
        while nodo_actual.get_izquierda() is not None:
            nodo_actual = nodo_actual.get_izquierda()
        return nodo_actual

    # Método para verificar si el arbol esta vacio
    def vacio(self):    
        '''
            Verifica si el árbol binario está vacío.

            Returns:
                bool: True si el árbol está vacío, False en caso contrario.
        '''
        return self.__raiz is None

    # Metodo que devuelve la cantidad de nodos en el arbol
    def cantidad(self):
        '''
            Devuelve la cantidad de nodos en el árbol binario.

            Returns:
                int: Cantidad de nodos en el árbol.
        '''
        return self.__cantidad_recursivo(self.__raiz)
    
    # Método privado para contar los nodos de forma recursiva
    def __cantidad_recursivo(self, nodo_actual: Node):
        '''
            Método privado que cuenta los nodos en el árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                int: Cantidad de nodos en el árbol.
        '''
        # Verificamos si el nodo actual es None
        if nodo_actual is None:
            return 0
        else:
            # Contamos el nodo actual y sumamos los nodos del subárbol izquierdo y derecho
            return 1 + self.__cantidad_recursivo(nodo_actual.get_izquierda()) + self.__cantidad_recursivo(nodo_actual.get_derecha())

    # Método para obtener la altura del árbol binario
    def altura(self):
        '''
            Devuelve la altura del árbol binario.

            Returns:
                int: Altura del árbol.
        '''
        return self.__altura_recursivo(self.__raiz)
    
    # Método privado para calcular la altura de forma recursiva
    def __altura_recursivo(self, nodo_actual: Node):
        '''
            Método privado que calcula la altura del árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                int: Altura del árbol.
        '''
        # Verificamos si el nodo actual es None
        if nodo_actual is None:
            return 0
        else:
            # Calculamos la altura del subárbol izquierdo y derecho y devolvemos el máximo
            return 1 + max(self.__altura_recursivo(nodo_actual.get_izquierda()), self.__altura_recursivo(nodo_actual.get_derecha()))

    # Metodo para obtener el numero de hojas del arbol binario
    def hojas(self):
        '''
            Devuelve el número de hojas del árbol binario.

            Returns:
                int: Número de hojas en el árbol.
        '''
        return self.__hojas_recursivo(self.__raiz)
    
    # Método privado para contar las hojas de forma recursiva
    def __hojas_recursivo(self, nodo_actual: Node):
        '''
            Método privado que cuenta las hojas en el árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                int: Número de hojas en el árbol.
        '''
        # Verificamos si el nodo actual es None
        if nodo_actual is None:
            return 0
        # Verificamos si el nodo es hoja (sin hijos)
        elif nodo_actual.get_izquierda() is None and nodo_actual.get_derecha() is None:
            return 1
        else:
            # Contamos las hojas del subárbol izquierdo y derecho
            return self.__hojas_recursivo(nodo_actual.get_izquierda()) + self.__hojas_recursivo(nodo_actual.get_derecha())

    # Método para buscar un nodo en el árbol binario
    def buscar(self, valor: int):
        '''
            Busca un nodo en el árbol binario.

            Parameters:
                valor (int): Valor del nodo a buscar.  
            Returns:
                bool: True si el nodo existe, False en caso contrario.
        '''
        return self.__buscar_recursivo(self.__raiz, valor)
    
    # Método privado para buscar un nodo de forma recursiva
    def __buscar_recursivo(self, nodo_actual: Node, valor: int):
        '''
            Método privado que busca un nodo en el árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
                valor (int): Valor del nodo a buscar.
            Returns:
                bool: True si el nodo existe, False en caso contrario.  
        '''
        # Verificamos si el nodo actual es None
        if nodo_actual is None:
            return False
        # Comparamos el valor del nodo actual con el valor buscado
        if nodo_actual.get_valor() == valor:
            return True
        elif valor < nodo_actual.get_valor():
            return self.__buscar_recursivo(nodo_actual.get_izquierda(), valor)
        else:
            return self.__buscar_recursivo(nodo_actual.get_derecha(), valor)
        
    # Metodo para realizar un recorrido inorden del árbol binario, este recorrido devuelve los nodos en orden ascendente 
    def inorden(self):  
        '''
            Realiza un recorrido inorden del árbol binario.

            Returns:
                list: Lista de valores en orden inorden.
        '''
        return self.__inorden_recursivo(self.__raiz)
    
    # Método privado para realizar un recorrido inorden de forma recursiva
    def __inorden_recursivo(self, nodo_actual: Node):
        '''
            Método privado que realiza un recorrido inorden del árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                list: Lista de valores en orden inorden.
        '''
        if nodo_actual is not None:
            return self.__inorden_recursivo(nodo_actual.get_izquierda()) + [nodo_actual.get_valor()] + self.__inorden_recursivo(nodo_actual.get_derecha())
        else:
            return []
        
    # Método para realizar un recorrido preorden del árbol binario, este recorrido devuelve los nodos en orden descendente
    def preorden(self):
        '''
            Realiza un recorrido preorden del árbol binario.

            Returns:
                list: Lista de valores en orden preorden.
        '''
        return self.__preorden_recursivo(self.__raiz)
    
    # Método privado para realizar un recorrido preorden de forma recursiva
    def __preorden_recursivo(self, nodo_actual: Node):
        '''
            Método privado que realiza un recorrido preorden del árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                list: Lista de valores en orden preorden.
        '''
        if nodo_actual is not None:
            return [nodo_actual.get_valor()] + self.__preorden_recursivo(nodo_actual.get_izquierda()) + self.__preorden_recursivo(nodo_actual.get_derecha())
        else:
            return []   
        
    # Método para realizar un recorrido postorden del árbol binario, este recorrido devuelve los nodos en orden descendente
    def postorden(self):
        '''
            Realiza un recorrido postorden del árbol binario.

            Returns:
                list: Lista de valores en orden postorden.
        '''
        return self.__postorden_recursivo(self.__raiz)
    
    # Método privado para realizar un recorrido postorden de forma recursiva
    def __postorden_recursivo(self, nodo_actual: Node):
        '''
            Método privado que realiza un recorrido postorden del árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                list: Lista de valores en orden postorden.
        '''
        if nodo_actual is not None:
            return self.__postorden_recursivo(nodo_actual.get_izquierda()) + self.__postorden_recursivo(nodo_actual.get_derecha()) + [nodo_actual.get_valor()]
        else:
            return []
    
    # Metodo que dibuja el arbol binario en la consola
    def dibujar(self):
        '''
            Dibuja el árbol binario en la consola.

            Returns:
                None
        '''
        self.__dibujar_recursivo(self.__raiz, 0)
    
    # Método privado para dibujar el árbol binario de forma recursiva
    def __dibujar_recursivo(self, nodo_actual: Node, nivel: int):
        '''
            Método privado que dibuja el árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
                nivel (int): Nivel del nodo actual.
            Returns:
                None
        '''
        if nodo_actual is not None:
            self.__dibujar_recursivo(nodo_actual.get_derecha(), nivel + 1)
            print("     " * nivel + str(nodo_actual.get_valor()))
            self.__dibujar_recursivo(nodo_actual.get_izquierda(), nivel + 1)
        else:
            print("     " * nivel)

    # Metodo para dibujar el arbol binario con sus conexiones
    def dibujar_con_conexiones(self):
        '''
            Dibuja el árbol binario con sus conexiones.

            Returns:
                None
        '''
        self.__dibujar_con_conexiones_recursivo(self.__raiz, 0) 

    # Método privado para dibujar el árbol binario con sus conexiones de forma recursiva
    def __dibujar_con_conexiones_recursivo(self, nodo_actual: Node, nivel: int):
        '''
            Método privado que dibuja el árbol binario con sus conexiones de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
                nivel (int): Nivel del nodo actual.
            Returns:
                None
        '''
        if nodo_actual is not None:
            self.__dibujar_con_conexiones_recursivo(nodo_actual.get_derecha(), nivel + 1)
            print("     " * nivel + str(nodo_actual.get_valor()))
            self.__dibujar_con_conexiones_recursivo(nodo_actual.get_izquierda(), nivel + 1)
        else:
            print("     " * nivel)
            print("     " * nivel + "|")
