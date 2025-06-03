'''
    Title: Proyecto principal que ejecuta la clase MCTS
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 12/05/2025
    Version: 1.1
'''


# Importamos la clase MCTS
from Clase_MCTS import MCTS


if __name__ == "__main__":
    mcts = MCTS(i=1000)
    mejor_apuesta = mcts.search()
    mcts.imprimir_arbol()
    print(f"La IA recomienda apostar a: {mejor_apuesta}")