'''
    Title: Una clase que simule el comportamiento de un dado
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 24/03/2025
    Version: 1.0 
'''


# Importamos la libreria random para generar numeros aleatorios
import random


# Definimos la clase Dado
class Dado:
    '''
        Clase que simula el comportamiento de un dado

        Attributes:
            caras (int): Número de caras del dado (por defecto 6).
            valor (int): Valor actual del dado despues del lanzamiento.
    '''

    def __init__(self, caras: int = 6):
        '''
            Metodo constructor de la clase

            Parameters:
                caras (int): Número de caras del dado (por defecto 6).
        '''
        # Definimos las variables privadas de la clase
        self.__caras = caras
        self.__valor = 1

    # Métodos Getter y Setter para 'caras'
    def get_caras(self):
        '''Devuelve el numero de caras del dado'''
        return self.__caras

    def set_caras(self, caras: int):
        """Establece el número de caras del dado."""
        #Verificamos que el número de caras sea mayor o igual a 2
        if caras >= 2:
            self.__caras = caras
        else:
            print("El dado debe tener al menos 2 caras.")

    # Método Getter para 'valor'
    def get_valor(self):
        """Devuelve el valor actual del dado."""
        return self.__valor

    def lanzar(self):
        """Lanza el dado y actualiza su valor."""
        self.__valor = random.randint(1, self.__caras)

    def __str__(self):
        """Devuelve una representación en string del dado."""
        return "Dado con " + str(self.__caras) + " caras. Último valor: " + str(self.__valor)
