'''
    Title: Una clase que implementa los atributos y metodos de un Nodo
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 01/04/2025
    Version: 1.0
'''


class Node:
    '''
        Clase que simula el comportamiento de un nodo en un árbol binario

        Attributes:
            valor (int): Valor del nodo.
            izquierda (Nodo): Nodo izquierdo.
            derecha (Nodo): Nodo derecho.
    '''

    def __init__(self, valor: int):
        '''
            Metodo constructor de la clase

            Parameters:
                valor (int): Valor del nodo.
        '''
        # Definimos las variables privadas de la clase
        self.__valor = valor
        self.__izq = None
        self.__der= None
    
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
    
    def __str__(self):
        '''Devuelve una representación en string del nodo'''
        return "Nodo con valor: " + str(self.__valor) + ", izquierda: " + str(self.__izq) + ", derecha: " + str(self.__der)
    