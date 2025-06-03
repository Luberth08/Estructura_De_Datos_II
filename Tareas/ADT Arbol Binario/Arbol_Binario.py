'''
    Title: Una clase que implementa los atributos y metodos de un Arbol Binario
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 01/04/2025
    Version: 1.1
'''


# Importamos la clase Node desde el archivo Nodo.py
from Nodo import Node
from collections import deque


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

    # Método para insertar un nuevo nodo en el árbol binario
    def insertar_nodo(self, valor: int):
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
                nuevo_nodo.set_padre(nodo_actual)
            else:
                self.__insertar_recursivo(nodo_actual.get_izquierda(), nuevo_nodo)
        else:
            # Si el nodo derecho es None, insertamos el nuevo nodo
            # Si no, seguimos buscando en el subárbol derecho
            if nodo_actual.get_derecha() is None:
                nodo_actual.set_derecha(nuevo_nodo)
                nuevo_nodo.set_padre(nodo_actual)
            else:
                self.__insertar_recursivo(nodo_actual.get_derecha(), nuevo_nodo)
    
    # Método para verificar si el arbol esta vacio
    def es_vacio(self):    
        '''
            Verifica si el árbol binario está vacío.

            Returns:
                bool: True si el árbol está vacío, False en caso contrario.
        '''
        return self.__raiz is None
    
    # Metodo para buscar un nodo en el arbol binario
    def buscar_x(self, valor: int):
        '''
            Busca un nodo en el árbol binario.

            Parameters:
                valor (int): Valor del nodo a buscar.  
            Returns:
                Node: Nodo encontrado o None si no existe.
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
                Node: Nodo encontrado o None si no existe.  
        '''
        # Verificamos si el nodo actual es None
        if nodo_actual is None:
            return None
        # Comparamos el valor del nodo actual con el valor buscado
        if nodo_actual.get_valor() == valor:
            return nodo_actual
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
    
    # Método para eliminar un nodo del árbol binario
    def eliminar_nodo(self, valor: int):
        '''
            Elimina un nodo del árbol binario de forma iterativa.

            Parameters:
                valor (int): Valor del nodo a eliminar.
        '''
        
        # Buscamos el nodo a eliminar
        nodo_actual = self.buscar_x(valor)

        # Si el nodo no existe, salimos del método
        if nodo_actual is None:
            return
        
        # Caso 1: Nodo sin hijos (hoja)
        if nodo_actual.es_hoja():
            if nodo_actual.get_padre() is not None:
                if nodo_actual.get_padre().get_izquierda() == nodo_actual:
                    nodo_actual.get_padre().set_izquierda(None)
                else:
                    nodo_actual.get_padre().set_derecha(None)
            else:
                self.__raiz = None
            return
        
        # Caso 2: Nodo con un hijo
        if nodo_actual.numero_hijos() == 1:
            if nodo_actual.get_izquierda() is not None:
                hijo = nodo_actual.get_izquierda()
            else:
                hijo = nodo_actual.get_derecha()

            if nodo_actual.get_padre() is not None:
                if nodo_actual.get_padre().get_izquierda() == nodo_actual:
                    nodo_actual.get_padre().set_izquierda(hijo)
                else:
                    nodo_actual.get_padre().set_derecha(hijo)
            else:
                self.__raiz = hijo

            hijo.set_padre(nodo_actual.get_padre())
            return
        
        # Caso 3: Nodo con dos hijos
        sucesor : Node = self.__buscar_sucesor(nodo_actual.get_derecha())
        valor_sucesor = sucesor.get_valor()
        self.eliminar_nodo(valor_sucesor)
        nodo_actual.set_valor(valor_sucesor)

    # Metodo privado para buscar el sucesor inorden del subarbol derecho
    def __buscar_sucesor(self, nodo_actual: Node):
        '''
            Método privado que busca el sucesor inorden de un nodo.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                Node: Sucesor inorden.
        '''
        # Buscamos el nodo más a la izquierda en el subárbol derecho
        if nodo_actual.get_izquierda() is not None:
            return self.__buscar_sucesor(nodo_actual.get_izquierda())
        else:
            return nodo_actual

    # Metodo para verificar si un nodo existe en el arbol binario
    def existe(self, valor: int):
        '''
            Verifica si un nodo existe en el árbol binario.

            Parameters:
                valor (int): Valor del nodo a verificar.
            Returns:
                bool: True si el nodo existe, False en caso contrario.
        '''
        return self.__buscar_recursivo(self.__raiz, valor) is not None

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

    # Metodo para el recorrido dfs del arbol binario
    def dfs(self):
        '''
            Realiza un recorrido en profundidad (DFS) del árbol binario.

            Returns:
                list: Lista de valores en orden DFS.
        '''
        return self.__dfs_recursivo(self.__raiz)

    # Método privado para el recorrido dfs de forma recursiva
    def __dfs_recursivo(self, nodo_actual: Node):
        '''
            Método privado que realiza un recorrido en profundidad (DFS) del árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
            Returns:
                list: Lista de valores en orden DFS.
        '''
        # Verificamos si el nodo actual no es None y no ha sido visitado
        if nodo_actual is not None:
            return [nodo_actual.get_valor()] + self.__dfs_recursivo(nodo_actual.get_izquierda()) + self.__dfs_recursivo(nodo_actual.get_derecha())
        else:
            return []

    # Método para el recorrido bfs del arbol binario
    def bfs(self):
        '''
            Realiza un recorrido en anchura (BFS) del árbol binario.

            Returns:
                list: Lista de valores en orden BFS.
        '''
        return self.__bfs_recursivo(self.__raiz)
    
    # Método privado para el recorrido bfs del arbol binario de forma recursiva
    def __bfs_recursivo(self, nodo_actual: Node, cola=None, visitados=None):
        '''
            Método privado que realiza un recorrido en anchura (BFS) del árbol binario de forma recursiva.

            Parameters:
                nodo_actual (Node): Nodo actual en la iteración.
                cola (deque): Cola de nodos por visitar.
                visitados (list): Lista de nodos visitados.
            Returns:
                list: Lista de valores en orden BFS.
        '''
        # Inicializamos la cola y la lista de visitados en la primera llamada
        if cola is None:
            cola = deque([nodo_actual])
            visitados = []

        # Verificamos si la cola está vacía
        if not cola:
            return visitados

        # Desencolamos el nodo actual
        nodo = cola.popleft()
        
        # Verificamos si el nodo actual no es None
        if nodo is not None:
            visitados.append(nodo.get_valor())
            cola.append(nodo.get_izquierda())
            cola.append(nodo.get_derecha())

        return self.__bfs_recursivo(None, cola, visitados)
    
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
