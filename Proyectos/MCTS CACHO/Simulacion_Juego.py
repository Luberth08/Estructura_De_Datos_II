'''
    Title: Proyecto principal que ejecuta la clases creadas
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''


# Importamos la clase MCTS
from Clase_Dados import Dados
from Clase_MCTS_Cacho import MCCTS

if __name__ == "__main__":
    arbol = MCCTS(i=10000, c=1.41)
    mano = Dados()
    mano.lanzar()
    mano.set_dados([3,2,2,5,1])
    arbol.get_root().set_mano(mano)
    resultado = arbol.search()
    arbol.imprimir_arbol()
    print(f"Primer tiro y sale:{mano.get_dados()}")
    print(f"la IA recomienda: apostar a {resultado[0].name} y lanzar los siguientes dados {resultado[1]}")



