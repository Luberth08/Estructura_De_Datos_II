'''
    Title: Una clase que implementa los atributos y metodos de un Nodo de Apuesta
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''


# Importamos librerias y clases que nos ayudaran en el proceso
from .Clase_NodoB import NodeB
from .Clase_NodoET import NodeET
from .Clase_Jugada import Jugada


class NodeA(NodeB):
    '''
        Clase que simula el comportamiento de un nodo de apuesta

        Attributes:
            jugada (Jugada): La jugada en cuestion
    '''

    def __init__(self, parent=None, jugada=Jugada.GRANDE):
        '''
            Metodo constructor de la clase

            Parameters:
                parent (Node): Nodo padre, vacio por defecto
                jugada (Jugada): la jugada en si
        '''
        super().__init__(parent) 
        self.__jugada = jugada
        self.__current_comb = 1  # Contador interno para combinaciones (1 a 31)

    # Sobreescribimos el metodo Setter para 'children'
    def set_children(self, children: list):
        '''Establece los hijos del nodo'''
        for child in children:
            if not isinstance(child, NodeET):  # Verifica que sea instancia de NodeET
                return  
        self._NodeB__children = children

    # Metodos Getter y Setter para 'jugada'
    def get_jugada(self):
        '''Devuelve la jugada'''
        return self.__jugada
    
    def set_jugada(self, jugada: Jugada):
        '''Establece la jugada'''  
        self.__jugada = jugada

    # Funcion que devuelve si el nodo esta totalmente expandido, osea si tiene todas las jugadas como hijos
    def is_fully_expanded(self):
        '''
            Verifica si el nodo esta completamente expandido
        
            Returns:
                bool: True si lo esta, False si no
        '''
        return self.__current_comb > 31  # 2^5 - 1; 5 dados, -1 porque no consideraremos la jugada [0,0,0,0,0] como valida

    # Metodo que expande el nodo actual agregandole un nuevo hijo
    def expand(self):
        '''
            Expande el nodo creando hijos para todas las jugadas posibles que no existen aún,

            Returns:
                Node :  Retorna el nuevo hijo creado, o None si ya está completamente 
                expandido o no puede expandirse mas.
        '''
        if self.is_fully_expanded():
            return None

        # Generar combinaciones en orden de "dados a conservar" (más 0's primero)
        while self.__current_comb <= 31: 
            # Convertir a binario de 5 bits: ej. 1 → 00001 → [0,0,0,0,1]
            comb = [int(bit) for bit in f"{self.__current_comb:05b}"]
            
            comb = comb[::-1]  # Invertir el orden de los bits
            
            self.__current_comb += 1  # Avanzar al siguiente número

            # Verificar si ya existe un hijo con esta combinación
            existing = any(
                child.get_lanzada() == comb
                for child in self.get_children()
            )

            if not existing:
                nuevo_hijo = NodeET(parent=self, lanzada=comb)
                self.get_children().append(nuevo_hijo)
                return nuevo_hijo