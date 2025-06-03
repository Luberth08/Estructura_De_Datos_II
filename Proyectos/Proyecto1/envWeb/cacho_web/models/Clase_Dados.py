'''
    Title: Una clase que implementa los atributos y metodos de un conjunto de 5 dados
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 14/05/2025
    Version: 1.1
'''


# Importamos librerias que nos ayudaran en el proceso
import random


class Dados:
    '''
        Clase que simula el comportamiento de un conjunto de 5 dados

        Attributes:
            dados (list): Una lista donde cada elemento representara el valor de un dado
    '''   

    def __init__(self):
        '''
            Metodo constructor de la clase
        '''
        self.__dados = [1,1,1,1,1]

    # Metodos Getter y Setter para 'dados'
    def get_dados(self):
        '''Devuelve el valor de los dados'''
        return self.__dados 
    
    def set_dados(self, dados: list):
        '''Establece el valor de los dados'''  
        if len(dados) != 5:
            return
        for d in dados:
            if d not in [1,2,3,4,5,6]:
                return
        self.__dados = dados

    # Metodo que lanza los dados aleatoriamente
    def lanzar(self, criterio: list = [1,1,1,1,1]):
        '''
            Simula el lanzamiento de los dados aleatoriamente

            Parameters:
                criterio (list): Una lista de 5 elementos (unos y ceros) que indicara 
                que dados lanzar y cuales no.
        '''
        if len(criterio) != 5:
            return
        
        for e in criterio:
            if e not in [1,0]:
                return
            
        for i in range(0,5):
            if criterio[i] == 1:
                self.__dados[i] = random.randint(1, 6)

    # Métodos para verificar si la jugada es "PAR"
    def es_par(self):
        '''
            Verifica si los dados forman un "doble" (dos pares y un desigual).
            
            Returns:
                bool: True si es doble, False si no.
        '''
        counts = {}
        for num in self.__dados:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.values(), reverse=True)
        return sorted_counts == [2, 2, 1]

    # Métodos para verificar si la jugada es "TRICA"
    def es_trica(self):
        '''
            Verifica si los dados forman una "trica" (tres iguales y dos desiguales).
            
            Returns:
                bool: True si es trica, False si no.
        '''
        counts = {}
        for num in self.__dados:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.values(), reverse=True)
        return sorted_counts == [3, 1, 1]

    # Métodos para verificar si la jugada es "ESCALERA"
    def es_escalera(self):
        '''
            Verifica si los dados forman una escalera (1-2-3-4-5 o 2-3-4-5-6).
            
            Returns:
                bool: True si es escalera, False si no.
        '''
        sorted_dados = sorted(self.__dados)
        return sorted_dados in ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 3, 4, 5, 6])

    # Métodos para verificar si la jugada es "FULL"
    def es_full(self):
        '''
            Verifica si los dados forman un "full" (tres iguales y un par).
            
            Returns:
                bool: True si es full, False si no.
        '''
        counts = {}
        for num in self.__dados:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.values(), reverse=True)
        return sorted_counts == [3, 2]

    # Métodos para verificar si la jugada es "POKER"
    def es_poker(self):
        '''
            Verifica si los dados forman un "póker" (cuatro iguales).
            
            Returns:
                bool: True si es póker, False si no.
        '''
        counts = {}
        for num in self.__dados:
            counts[num] = counts.get(num, 0) + 1
        sorted_counts = sorted(counts.values(), reverse=True)
        return sorted_counts == [4, 1]

    # Métodos para verificar si la jugada es "GRANDE"
    def es_grande(self):
        '''
            Verifica si los dados forman "la grande" (cinco iguales).
            
            Returns:
                bool: True si es la grande, False si no.
        '''
        return len(set(self.__dados)) == 1
    
    # Método adicional: Verificar todas las jugadas posibles
    def obtener_jugada(self):
        '''
            Determina la jugada más alta posible con los dados actuales.
            
            Returns:
                str: Nombre de la jugada (ej: "escalera", "full", etc.).
        '''
        if self.es_grande():
            return 6
        elif self.es_poker():
            return 5
        elif self.es_full():
            return 4
        elif self.es_escalera():
            return 3
        elif self.es_trica():
            return 2
        elif self.es_par():
            return 1
        else:
            return 0

    def __str__(self):
        return "Mano: " + str(self.__dados)