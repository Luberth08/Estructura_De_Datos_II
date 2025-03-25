'''

Title: Juego Simple dE Dados
Author: Villarroel Gutierrez Josue Luberth 
Date: 24/03/2025
Version: 1.0

'''


# Importamos la libreria random para generar numeros aleatorios.
import random


def lanzar_dado():
    '''
        Funcion que simula el lanzamiento de un dado de seis caras.

        Parameters:
            None
        Returns:
            int: Numero aleatorio entre 1 y 6.
    '''
    return random.randint(1, 6)


def jugar():
    ''' 
        Simula una ronda de juego de dados.

        Parameters:
            None

        Returns:
            None
    '''
    # Mensaje de bienvenida
    print("🎲 ¡Bienvenido al juego de dados! 🎲\n")

    # Turno del Jugador
    input("Presiona ENTER para lanzar tu dado... ")
    dado_usuario = lanzar_dado()
    print("Tu resultado ha sido: " + str(dado_usuario) + "\n")

    # Turno de la Computadora
    print("La computadora está lanzando el dado..."+"\n")
    dado_comp = lanzar_dado()
    print("El resultado de la computadora es:" + str(dado_comp)+"\n")

    # Determinar al ganador
    if dado_usuario > dado_comp:
        print("🎉 ¡Ganaste! 🎉")
    elif dado_usuario < dado_comp:
        print("😢 Perdiste. La computadora ganó.")
    else:
        print("🤝 ¡Empate! Ambos sacaron el mismo número.")  


if __name__ == "__main__":
    # Iniciar el juego
    jugar()

