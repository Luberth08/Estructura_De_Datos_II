'''
    Title: Una clase que implementa los atributos y metodos de un Nodo de Estrategia de Tiro
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''


# Importamos librerias y clases que nos ayudaran en el proceso
from .Clase_NodoB import NodeB


class NodeET(NodeB):
    '''
        Clase que simula el comportamiento de un nodo de Estrategia de Tiro

        Attributes:
            lanzada (list): Una lista de 5 elementos(unos y ceros) que determinan
            que dado se lanza y cual no
    '''

    def __init__(self, parent=None, lanzada=None):
        '''
            Metodo constructor de la clase

            Parameters:
                parent (Node): Nodo padre, vacio por defecto
                lanzada (list): La lista de dados que se va lanzar
        '''
        super().__init__(parent) 
        self.__lanzada = lanzada 

    # Metodos Getter y Setter para 'lanzada'
    def get_lanzada(self):
        '''Devuelve la lista de dados a lanzar'''
        return self.__lanzada
    
    def set_lanzada(self, lanzada: list):
        '''Establece los dados a lanzar'''  
        if len(lanzada) != 5:
            return
        for i in lanzada:
            if i not in [1,0]:
                return
        self.__lanzada = lanzada
    
    def is_fully_expanded(self) -> bool:
        # Los nodos terminales (NodeET) no se pueden expandir
        return True