'''
    Title: Una clase que implementa los atributos y metodos de un Nodo de Dados
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''


# Importamos librerias y clases que nos ayudaran en el proceso
from .Clase_NodoB import NodeB
from .Clase_NodoA import NodeA
from .Clase_Dados import Dados
from .Clase_Jugada import Jugada


class NodeD(NodeB):
    '''
        Clase que simula el comportamiento de un nodo de dados

        Attributes:
            mano (Dados): Un conjunto de 5 dados que se tienen en la mano
    '''

    def __init__(self, parent=None, mano=Dados()):
        '''
            Metodo constructor de la clase

            Parameters:
                parent (Node): Nodo padre, vacio por defecto
                mano (Dados): El conjunto de dados de la mano
        '''
        super().__init__(parent) 
        self.__mano = mano  
        self.__jugadas = {Jugada.PAR: 1, Jugada.TRICA: 1, Jugada.ESCALERA: 1, Jugada.FULL: 1, Jugada.POKER: 1, Jugada.GRANDE: 1}

    # Sobreescribimos el metodo Setter para 'children'
    def set_children(self, children: list):
        '''Establece los hijos del nodo'''
        for child in children:
            if not isinstance(child, NodeA):  # Verifica que sea instancia de NodeA
                return  
        self._NodeB__children = children

    # Metodos Getter y Setter para 'mano'
    def get_mano(self):
        '''Devuelve el atributo mano'''
        return self.__mano
    
    def set_mano(self, mano: Dados):
        '''Establece el valor de la mano'''  
        self.__mano = mano

    # Metodos Getter y Setter para 'jugadas'
    def get_jugadas(self):
        '''Devuelve el atributo mano'''
        return self.__jugadas
    
    def set_jugadas(self, jugadas: dict):
        '''Establece el valor de la mano'''  
        self.__jugadas = jugadas

    # Funcion que devuelve si el nodo esta totalmente expandido, osea si tiene todas las jugadas como hijos
    def is_fully_expanded(self):
        '''
            Verifica si el nodo esta completamente expandido a todas las jugadas posibles
        
            Returns:
                bool: True si lo esta, False si no
        '''
        n = 0
        for jugada in Jugada:
            if self.__jugadas.get(jugada, 0) == 1:
                n += 1
        return len(self._NodeB__children) == n
    
    # Modificamos la funcion best_child
    def best_child(self, c: float):
        '''
            Versión modificada que selecciona el mejor hijo considerando:
            1. Mayor valor UCT
            2. En caso de empate, mayor prioridad de jugada

            Parameters:
                c (float): la constante de exploracion
            Returns:
                NodeB: Hijo con mayor UCT y mejor jugada
        '''
        hijos = self.get_children()
        
        if not hijos:
            return None

        # Obtenemos el máximo valor UCT
        max_uct = max(child.uct(c) for child in hijos)
        
        # Filtramos los hijos con máximo UCT
        mejores = [child for child in hijos if child.uct(c) == max_uct]
            
        # Ordenar por prioridad de jugada (asumiendo que Jugada está ordenado por importancia)
        mejores_ord = sorted(
            mejores,
            key=lambda x: x.get_jugada().value,  # Usamos el valor del Enum como prioridad
            reverse=True
        )
        
        return mejores_ord[0]

    # Metodo que expande el nodo actual agregandole un nuevo hijo
    def expand(self):
        '''
            Expande el nodo creando hijos para todas las jugadas posibles que no existen aún,
            Devuelve el primer hijo no creado anteriormente

            Returns:
                Node :  Retorna el nuevo hijo creado, o None si ya está completamente 
                expandido o no puede expandirse mas.
        '''
        # Verificar si ya está completamente expandido
        if self.is_fully_expanded():
            return None

        # Obtener jugadas existentes en los hijos actuales
        jugadas_existentes = [hijo.get_jugada() for hijo in self.get_children()]

        # Crear nuevos hijos para las jugadas faltantes
        for jugada in Jugada:
            if self.__jugadas.get(jugada, 0) == 1 and jugada not in jugadas_existentes:
                nuevo_hijo = NodeA(parent=self, jugada=jugada)
                self.get_children().append(nuevo_hijo)
                return nuevo_hijo