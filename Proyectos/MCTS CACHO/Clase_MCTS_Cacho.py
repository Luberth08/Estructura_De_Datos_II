'''
    Title:  Una clase que implementa los atributos y metodos 
            de un Arbol de busqueda de Cacho Monte Carlo (MCCTS)
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''


#Importamos lo necesario para poder diseñar la clase
import copy


# Importamos las clases Nodos
from Clase_NodoD import NodeD
from Clase_NodoA import NodeA
from Clase_NodoET import NodeET
from Clase_NodoB import NodeB
from Clase_Jugada import Jugada


class MCCTS:
    '''
        Clase que simula el comportamiento de un Arbol de busqueda para Caho Monte Carlo

        Attributes:
            root (NodeD): Nodo raiz, contiene la combinacion de dados inicial
            i (int): Cantidad de simulaciones a realizar, por defecto 1000
            C (float): Constante de exploracion, por defecto 1,41
    '''

    def __init__(self, i=1000, c=1.41):
        '''
            Metodo constructor de la clase

            Parameters:
                i (int): Cantidad de simulaciones a realizar, por defecto 1000
                C (float): Constante de exploracion, por defecto 1,41
        '''
        self.__root = NodeD()
        self.__i = i
        self.__c = c

    # Metodos Getter y Setter para 'root'
    def get_root(self):
        '''Devuelve el nodo raiz'''
        return self.__root
    
    def set_root(self, root: NodeD):
        '''Establece el nodo raiz'''  
        self.__root = root

    # Metodos Getter y Setter para 'i'
    def get_i(self):
        '''Devuelve el numero de iteraciones'''
        return self.__i
    
    def set_i(self, i: int):
        '''Establece el numero de iteraciones'''  
        if i < 1:
            return
        self.__i = i

    # Metodos Getter y Setter para 'c'
    def get_c(self):
        '''Devuelve la constante de exploracion'''
        return self.__c
    
    def set_c(self, c: float):
        '''Establece la constante de exploracion'''  
        self.__c = c

    # Funcion que simula una partida tomando la jugada apostada y el lanzamiento resividos y devuelve el resultado
    def simulate(self, jugada: Jugada, lanzada: list):
        '''
            Simula una partida tomando la jugada apostada y el lanzamiento resividos y luego devuelve el resultado

            Parameters:
                jugada (Jugada): la jugada apostada
                lanzada (list): el criterio de lanzamiento
            Returns:
                int: resultado de la partida simulada
        '''
        # Generamos una copia de la mano actual para no modificar la principal
        mano_actual = copy.deepcopy(self.__root.get_mano())

        # Lanzamos los dados con el criterio de lanzamiento
        mano_actual.lanzar(lanzada)

        # Recompensa: 1 saco la jugada apostada, 0 si falló
        if mano_actual.obtener_jugada() == jugada:
            return jugada.puntos()
        else:
            return 0

    # Metodo que actualiza valores desde un nodo terminal hasta el nodo raiz
    def backpropagate(self, node: NodeB, reward: int):
        '''
            Actualiza valores desde un nodo terminal hasta el nodo raiz

            Parameters:
                node (NodeB): El ultimo nodo simulado en una iteracion
                reward (int): El resultado de la simulacion
        '''
        current_node = node
        while current_node is not None:
            current_node.set_n(current_node.get_n() + 1)
            current_node.set_q(current_node.get_q() + reward)
            current_node = current_node.get_parent()

    # Funcion que determina si un nodo es terminal o no
    def is_terminal(self, node: NodeB):
        '''
            Determina si un nodo es terminal o no, es terminal si el nodo es de tipo NodeET

            Parameters:
                node (NodeB): el nodo a evaluar
            Returns:
                bool: True si es terminal, False si no
        '''
        return isinstance(node, NodeET)

    # Funcion que ejecuta un numero fijo de simulaciones y que determina cual es la mejor accion inicial
    def search(self):
        '''
            Realiza todo el ciclo de MCTS: Selección, Expansión, Simulación y Retropropagación.
        '''
        for _ in range(self.__i):
            node = self.__root

            # 1. Selección
            while node.is_fully_expanded() and not self.is_terminal(node):
                node = node.best_child(self.__c)

            # 2. Expansión 
            if not self.is_terminal(node) and not node.is_fully_expanded():
                new_node = node.expand()
                if new_node is not None:
                    node = new_node

            if isinstance(node, NodeET):
                # 3. Simulación
                reward = self.simulate(node.get_parent().get_jugada(), node.get_lanzada())
                # 4. Backpropagation
                self.backpropagate(node, reward)

        # Elegimos la mejor jugada, el que fue mas visitado
        mejor_jugada = max(self.__root.get_children(), key=lambda n: n.get_n())
        # Finalmente, elegimos la mejor estrategia de tiro de esa    
        mejor_lanzada = max(mejor_jugada.get_children(), key=lambda n: n.get_n())

        return [mejor_jugada.get_jugada(), mejor_lanzada.get_lanzada()]
    
    # Metodo que bloquea una jugada en el arbol
    def bloquear_jugada(self, jugada: Jugada):
        '''
            Bloquea una jugada en el arbol, para que no se pueda volver a elegir

            Parameters:
                jugada (int): la jugada a bloquear
        '''
        self.__root.get_jugadas()[jugada] = 0
        
    # Metodo que imprime el arbol en consola
    def imprimir_arbol(self):
        '''
            Imprime el árbol desde la raíz en consola con indentación para ver la estructura jerárquica.
        '''
        def imprimir_nodo(node, nivel=0):
            indent = "  " * nivel
            if isinstance(node, NodeD):
                print(f"{indent}- Mano: {node.get_mano()}, Q: {node.get_q()}, N: {node.get_n()}")
            elif isinstance(node, NodeA):
                print(f"{indent}- jugada: {node.get_jugada()}, Q: {node.get_q()}, N: {node.get_n()}")
                pass
            else:
                print(f"{indent}- lanzada: {node.get_lanzada()}, Q: {node.get_q()}, N: {node.get_n()}")
                pass

            for hijo in node.get_children():
                imprimir_nodo(hijo, nivel + 1)

        print("Árbol MCCTS:")
        imprimir_nodo(self.__root)