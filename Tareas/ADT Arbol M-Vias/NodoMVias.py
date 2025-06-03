'''
    Title: Una clase que implementa los atributos y metodos de un Nodo de un arbol M-Vias
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 02/06/2025
    Version: 1.1
'''


class NodoMVias:
    '''
        Clase que representa un nodo en un árbol m-vías (árbol B).
    
        Atributos:
            claves (list): Lista de claves almacenadas en el nodo (tamaño: m-1).
            hijos (list): Lista de punteros a los hijos del nodo (tamaño: m).
            n (int): Número actual de claves no nulas en el nodo.
    '''
    
    def __init__(self, m):
        '''
            Constructor del nodo M-Vías.
            
            Parámetros:
                m (int): Orden del árbol (número máximo de hijos por nodo).
        '''
        self.claves = [None] * (m - 1)  # Claves inicializadas a None
        self.hijos = [None] * m          # Hijos inicializados a None
        self.n = 0          # Contador de claves válidas

    # Metodos Getter y Setter para 'claves'
    def get_clave(self, indice):
        '''
            Obtiene una clave específica de un indice dado del nodo.
        '''
        if 0 <= indice < len(self.claves):
            return self.claves[indice]
        raise IndexError("Índice de clave fuera de rango")
    
    def get_claves(self):
        '''
            Retorna la lista completa de claves (para operaciones internas).
        '''
        return self.claves

    def set_clave(self, indice, valor):
        '''
            Modifica una clave específica del nodo.
            
            Parámetros:
                indice (int): Posición de la clave a modificar.
                valor (any): Nuevo valor para la clave.
        '''
        if 0 <= indice < len(self.claves):
            self.claves[indice] = valor
        else:
            raise IndexError("Índice de clave fuera de rango")

    # Metodos Getter y Setter para 'hijos'
    def get_hijo(self, indice):
        '''
            Obtiene un hijo específico de un indice dado del nodo.
        '''
        if 0 <= indice < len(self.hijos):
            return self.hijos[indice]
        raise IndexError("Índice de hijo fuera de rango")
    
    def get_hijos(self):
        '''
            Retorna la lista completa de hijos (para operaciones internas).
        '''
        return self.hijos
    
    def set_hijo(self, indice, nodo):
        '''
            Modifica un hijo específico del nodo.
            
            Parámetros:
                indice (int): Posición del hijo a modificar.
                nodo (NodoMVias): Nuevo nodo hijo.
        '''
        if 0 <= indice < len(self.hijos):
            self.hijos[indice] = nodo
        else:
            raise IndexError("Índice de hijo fuera de rango")

    # Metodos Getter 'n'
    def get_n(self):
        '''
            Retorna el número de claves válidas en el nodo.
        '''
        return self.n

    def es_hoja(self):
        '''
            Verifica si el nodo es una hoja (todos sus hijos son None).
            
            Retorna:
                bool: True si es hoja, False en caso contrario.
        '''
        for hijo in self.hijos:
            if hijo is not None:
                return False
        return True

    def esta_lleno(self, m):
        '''
            Verifica si el nodo está lleno (contiene m-1 claves).
            
            Parámetros:
                m (int): Orden del árbol.
                
            Retorna:
                bool: True si está lleno, False en caso contrario.
        '''
        return self.n == m - 1
    
    def esta_vacio(self):
        '''
            Devuelve True si el nodo no tiene claves.
        '''
        return self.n == 0
