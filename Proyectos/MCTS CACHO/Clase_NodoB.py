'''
    Title: Una clase que implementa los atributos y metodos de un Nodo Base o Molde
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''


# Importamos librerias que nos ayuden con el proceso
import math


class NodeB:
    '''
        Clase que simula el comportamiento de un nodo Base

        Attributes:
            parent (NodeB): Nodo padre
            children (list): lista de nodos hijos
            Q (int): Suma de recompensas del nodo
            N (int): Numero de veces que se ha visitado este nodo
    '''

    def __init__(self, parent=None):
        '''
            Metodo constructor de la clase

            Parameters:
                parent (Node): Nodo padre, vacio por defecto
        '''
        self.__parent = parent       
        self.__children = []        
        self.__q = 0                
        self.__n = 0                

    # Metodos Getter y Setter para 'parent'
    def get_parent(self):
        '''Devuelve el nodo padre'''
        return self.__parent 
    
    def set_parent(self, parent: 'NodeB'):
        '''Establece el nodo padre'''  
        self.__parent = parent

    # Metodos Getter y Setter para 'children'
    def get_children(self):
        '''Devuelve los hijos del nodo'''
        return self.__children
    
    def set_children(self, children: list):
        '''Establece los hijos del nodo'''
        for child in children:
            if not isinstance(child, NodeB):  # Verifica que sea instancia de NodeB
                return  
        self.__children = children

    # Metodos Getter y Setter para 'q'
    def get_q(self):
        '''Devuelve el atributo q'''
        return self.__q
    
    def set_q(self, q: int):
        '''Establece el valor de q'''  
        self.__q = q

    # Metodos Getter y Setter para 'n'
    def get_n(self):
        '''Devuelve el atributo n'''
        return self.__n
    
    def set_n(self, n: int):
        '''Establece el valor de n'''  
        self.__n = n

    # Funcion que devuelve el UCT del nodo  
    def uct(self, c: float):
        '''
            Calcula la formula del UCT del nodo para la ayuda de toma de decisiones

            Parameters:
                c (float): la constante de exploracion
            Returns:
                float: El resultado de la formula
        '''
        if self.__n == 0:
            # Significa que el nodo aun no ha sido explorado, 
            # por lo que forzamos la exploracion inicial
            return float('inf')  
        return (self.__q / self.__n) + c * math.sqrt(math.log(self.__parent.get_n()) / self.__n)

    # Metodo que devuelve el mejor hijo mediante su UCT
    def best_child(self, c: float):
        '''
            Calcula el UCT de todos los hijos y elige el hijo que tenga el mayor UCT

            Parameters:
                c (float): la constante de exploracion
            Returns:
                NodeB: Hijo con mayor UCT
        '''
        return max(self.get_children(), key=lambda child: child.uct(c))