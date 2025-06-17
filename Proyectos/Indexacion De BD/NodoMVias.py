'''
    Title: Una clase que implementa los atributos y metodos de un nodo M-Vias para indexación de bases de datos.
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 10/06/2025
    Version: 1.0
'''


class NodoMVias:
    '''
        Nodo de un árbolMVias para indexación de bases de datos.
        Cada nodo almacena pares (clave, puntero) y referencias a hijos.

        Atributos:
            __claves (list): Lista de tuplas (clave, puntero) del nodo
            __hijos (list): Lista de referencias a nodos hijos
            __es_hoja (bool): Indica si el nodo es una hoja
            __padre (NodoMVias): Referencia al nodo padre
    '''
    
    def __init__(self):
        '''
            Inicializa el nodo del arbol M-Vias.
        '''

        self.__claves = []                # Tuplas (clave, puntero)
        self.__hijos = []                 # Referencias a nodos hijos
        self.__es_hoja = True             # Indica si el nodo es hoja
        self.__padre = None               # Padre del nodo
    
    # Metodos Getter y Setter para "claves"
    def get_claves(self):
        '''Devuelve la lista que contiene las claves del nodo'''
        return self.__claves

    def set_claves(self, claves: list):
        '''Establece la lista que contendra las claves del nodo'''   
        self.__claves = claves

    # Metodos Getter para "hijos"
    def get_hijos(self):
        '''Devuelve la lista que contiene los hijos del nodo''' 
        return self.__hijos
    
    def set_hijos(self, hijos: list):
        '''Establece la lista que contendra los hijos del nodo'''   
        self.__hijos = hijos

    # Metodos Getter y Setters para "padre"
    def get_padre(self):
        '''Devuelve el padre del nodo''' 
        return self.__padre
    
    def set_padre(self, padre: 'NodoMVias'):
        '''Establece el padre del nodo''' 
        self.__padre = padre

    # Metodos Getter y Setters para "es_hoja"
    def get_es_hoja(self):
        '''Devuelve si el nodo es hoja''' 
        return self.__es_hoja

    def set_es_hoja(self, es_hoja: bool):
        '''Establece si el nodo es hoja''' 
        self.__es_hoja = es_hoja

    # Funcion que busca la posicion indicada para una clave
    def buscar_pos(self, clave):
        '''
            Funcion que devuelve la posicion en la que deberia ser insertado la clave.

            Args:
                clave (int): La clave a insertar.
        '''
        if not self.__claves or clave >= self.__claves[-1][0]:
            return len(self.__claves)

        a, b = 0, len(self.__claves) - 1
        while a < b:
            p = (a + b) // 2
            if clave < self.__claves[p][0]:
                b = p
            else:
                a = p + 1
        return a
    
    # Metodo que inserta una clave en el nodo de manera ordenada
    def insertar(self, clave, puntero = None):
        '''
            Método que inserta ordenadamente la clave en el nodo.

            Args:
                clave (int): La clave a insertar.
        '''

        if not self.__claves:
            # Caso nodo vacío
            self.__claves = [(clave, puntero)]
            self.__hijos = [None, None]
            return

        p = self.buscar_pos(clave)
        self.__claves.insert(p, (clave, puntero))
        
        # Insertar un nuevo hijo (None) en posición p+1
        self.__hijos.insert(p + 1, None) 

    # Método para imprimir el nodo en consola
    def __str__(self): 
        res = f"Claves: {self.__claves}\n"
        
        # Mostrar estado de hoja
        res += f"├── Es hoja: {self.__es_hoja}\n"
        
        # Mostrar hijos
        nh = 0
        for i in self.__hijos:
            if i:
                nh += 1 

        res += f"└── Hijos ({nh}):\n"
        
        return res