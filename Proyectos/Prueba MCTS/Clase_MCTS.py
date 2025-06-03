'''
    Title:  Una clase que implementa los atributos y metodos 
            de un Arbol de busqueda Monte Carlo (MCTS)
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 12/05/2025
    Version: 1.1
'''


#Importamos lo necesario para poder diseñar la clase
import random


# Importamos la clase Nodo
from Clase_Node import Node


class MCTS:
    '''
        Clase que simula el comportamiento de un MCTS

        Attributes:
            root (Node): Nodo raiz
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
        self.__root = Node()
        self.__i = i
        self.__c = c

    # Metodos Getter y Setter para 'root'
    def get_root(self):
        '''Devuelve el nodo raiz'''
        return self.__root
    
    def set_root(self, root: Node):
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

    # Funcion que simula una partida tomando la accion resivida y devuelve el resultado
    def simulate(self, action):
        '''
            Simula una partida tomando la accion resivida y luego devuelve el resultado

            Parameters:
                action (str): la accion elegida, 'mayor' o 'menor'
            Returns:
                int: resultado de la partida simulada
        '''
        # Genera un número aleatorio entre 1 y 10 (el número secreto, desconocido)
        numero_secreto = random.randint(1, 10)

        # Recompensa: 1 si adivinó bien, 0 si falló
        if (action == 'mayor' and numero_secreto > 5) or \
            (action == 'menor' and numero_secreto < 5):
            return 1
        else:
            return 0

    # Metodo que actualiza valores desde un nodo hoja hasta el nodo raiz
    def backpropagate(self, node: Node, reward: int):
        '''
            Actualiza valores desde un nodo hoja hasta el nodo raiz

            Parameters:
                node (Node): El ultimo nodo simulado en una iteracion
                reward (int): El resultado de la simulacion
        '''
        if node is None:
            return
        
        node.set_n(node.get_n() + 1)
        node.set_q(node.get_q() + reward)
        self.backpropagate(node.get_parent(), reward)

    # Funcion que ejecuta un numero fijo de simulaciones y que determina cual es la mejor accion inicial
    def search(self):
        '''
            Realiza todo el ciclo de MCTS: Selección, Expansión, Simulación y Retropropagación.
        '''

        for _ in range(self.__i):
            node = self.__root

            # 1. Selección
            while node.is_fully_expanded():
                node = node.best_child(self.__c)

            # 2. Expansión
            if not node.is_fully_expanded() and not node.is_terminal():
                node = node.expand()

            # 3. Simulación
            reward = self.simulate(node.get_action())

            # 4. Backpropagation
            self.backpropagate(node, reward)

        # Finalmente, elegimos la mejor acción, el que fue mas visitado
        mejor_hijo = max(self.__root.get_children(), key=lambda n: n.get_n())
        return mejor_hijo.get_action()
    
    # Metodo que imprime el arbol en consola
    def imprimir_arbol(self):
        '''
            Imprime el árbol desde la raíz en consola con indentación para ver la estructura jerárquica.
        '''
        def imprimir_nodo(node, nivel=0):
            indent = "  " * nivel
            print(f"{indent}- Acción: {node.get_action()}, Q: {node.get_q()}, N: {node.get_n()}")
            for hijo in node.get_children():
                imprimir_nodo(hijo, nivel + 1)

        print("Árbol MCTS:")
        imprimir_nodo(self.__root)