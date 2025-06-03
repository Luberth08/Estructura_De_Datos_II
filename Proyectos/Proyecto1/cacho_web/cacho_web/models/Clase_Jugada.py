'''
    Title: Una clase que simula un enumerado de jugadas
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''
from enum import Enum


# Enumerado de las jugadas
class Jugada(Enum):
    NONE = 0
    PAR = 1
    TRICA = 2
    ESCALERA = 3
    FULL = 4
    POKER = 5
    GRANDE = 6

    def puntos(self):
        """
        Devuelve los puntos REALES según el Cacho.
        """
        return {
            Jugada.NONE: 0,
            Jugada.PAR: 5,
            Jugada.TRICA: 10,
            Jugada.ESCALERA: 20,
            Jugada.FULL: 30,
            Jugada.POKER: 40,
            Jugada.GRANDE: 50
        }[self]