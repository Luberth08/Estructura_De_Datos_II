'''
    Title: Una clase que implementa los atributos y metodos de un Nodo
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 01/04/2025
    Version: 1.1
'''


class Node:
    '''
        Clase que simula el comportamiento de un nodo en un árbol binario

        Attributes:
            valor (int): Valor del nodo.
            izquierda (Nodo): Nodo izquierdo.
            derecha (Nodo): Nodo derecho.
    '''

    def __init__(self, valor: int, padre: 'Node' = None):
        '''
            Metodo constructor de la clase

            Parameters:
                valor (int): Valor del nodo.
        '''
        # Definimos las variables privadas de la clase
        self.__valor = valor
        self.__izq = None
        self.__der= None
        self.__padre = padre
    
    # Metodos Getter y Setter para 'valor'
    def get_valor(self):
        '''Devuelve el valor del nodo'''
        return self.__valor 
    
    def set_valor(self, valor: int):
        '''Establece el valor del nodo'''  
        self.__valor = valor

    # Métodos Getter y Setter para 'izquierda'
    def get_izquierda(self):
        '''Devuelve el nodo izquierdo'''
        return self.__izq
    
    def set_izquierda(self, izq: 'Node'):
        '''Establece el nodo izquierdo'''
        self.__izq = izq

    # Métodos Getter y Setter para 'derecha'
    def get_derecha(self):
        '''Devuelve el nodo derecho'''  
        return self.__der
    
    def set_derecha(self, der: 'Node'):
        '''Establece el nodo derecho'''
        self.__der = der
    
    # Métodos Getter y Setter para 'padre'
    def get_padre(self):
        '''Devuelve el nodo padre'''
        return self.__padre
    
    def set_padre(self, padre: 'Node'):
        '''Establece el nodo padre'''
        self.__padre = padre

    # Método para verificar si el nodo es hoja
    def es_hoja(self):
        '''
            Verifica si el nodo es una hoja
        
            Returns:
                bool: True si el nodo es una hoja, False en caso contrario
        '''
        return self.__izq is None and self.__der is None

    # Método que devuelve la cantidad de hijos del nodo(minimo 0, maximo 2)
    def numero_hijos(self):
        '''
            Devuelve la cantidad de hijos del nodo

            Returns:
                int: Cantidad de hijos del nodo (0, 1 o 2)
        '''
        return int(self.__izq is not None) + int(self.__der is not None)

    def __str__(self):
        '''Devuelve una representación en string del nodo'''
        return "Nodo con valor: " + str(self.__valor) + ", izquierda: " + str(self.__izq) + ", derecha: " + str(self.__der)
    