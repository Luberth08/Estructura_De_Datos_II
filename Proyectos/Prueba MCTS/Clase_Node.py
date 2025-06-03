'''
    Title: Una clase que implementa los atributos y metodos de un Nodo
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 12/05/2025
    Version: 1.1
'''


# Importamos librerias que nos ayuden con el proceso
import math


class Node:
    '''
        Clase que simula el comportamiento de un nodo en un MCTS

        Attributes:
            parent (Node): Nodo padre
            children (list): lista de nodos hijos
            Q (int): Suma de recompensas del nodo
            N (int): Numero de veces que se ha visitado este nodo
            action (str): Accion que se eligio en este nodo('mayor' o 'menor')
    '''

    def __init__(self, parent=None, action=None):
        '''
            Metodo constructor de la clase

            Parameters:
                parent (Node): Nodo padre, vacio por defecto
                action (str): accion elegida, vacio por defecto
        '''
        self.__parent = parent       
        self.__children = []        
        self.__q = 0                
        self.__n = 0            
        self.__action = action       

    # Metodos Getter y Setter para 'parent'
    def get_parent(self):
        '''Devuelve el nodo padre'''
        return self.__parent 
    
    def set_parent(self, parent: 'Node'):
        '''Establece el nodo padre'''  
        self.__parent = parent

    # Metodos Getter y Setter para 'children'
    def get_children(self):
        '''Devuelve los hijos del nodo'''
        return self.__children
    
    def set_children(self, children: list):
        '''Establece los hijos del nodo'''  
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

    # Metodos Getter y Setter para 'action'
    def get_action(self):
        '''Devuelve el atributo action'''
        return self.__action
    
    def set_action(self, action: str):
        '''Establece el valor de action''' 
        if action != "mayor" and action != "menor":
            return 
        self.__action = action

    # Funcion que devuelve el nodo esta totalmente expandido, osea si tiene 2 hijos
    def is_fully_expanded(self):
        '''
            Verifica si el nodo esta completamente expandido
        
            Returns:
                bool: True si lo esta, False si no
        '''
        return len(self.__children) == 2 

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
                Node: Hijo con mayor UCT
        '''
        return max(self.get_children(), key=lambda child: child.uct(c))

    # Metodo que devuelve si el nodo ya no se puede expandir mas
    def is_terminal(self):
        '''
            Determina si el nodo se puede expandir mas o no

            Returns:
                bool: True si no se puede expandir, False si todavia puede expandirse
        '''
        return self.__action in ['mayor', 'menor']
    
    # Metodo que expande el nodo actual agregandole un nuevo hijo
    def expand(self):
        '''
            Expande el nodo con un nuevo hijo si aun no ha sido totalmente expandido 
            y si se puede expandir mas
            
            Returns:
                Node :  Retorna el nuevo hijo creado, o None si ya está completamente 
                expandido o no puede expandirse mas.
        '''
        if self.is_terminal() or self.is_fully_expanded():
            return None  # No se expande más

        acciones_posibles = ['mayor', 'menor']
        acciones_actuales = [child.get_action() for child in self.__children]

        for accion in acciones_posibles:
            if accion not in acciones_actuales:
                nuevo_hijo = Node(parent=self, action=accion)
                self.__children.append(nuevo_hijo)
                return nuevo_hijo