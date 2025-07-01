'''
    Title: Una clase que implementa un motor de indexación para una base de datos de estudiantes.
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 29/06/2025
    Version: 1.0
'''


import os
from BaseDeDatos import RegistroEstudiante
from ArbolMVias import ArbolMVias

class MotorIndexacion:
    '''
        Motor de indexación que utiliza un árbol M-Vías para indexar estudiantes por CI.
        
        Atributos:
            db (RegistroEstudiante): Base de datos de estudiantes
            arbol (ArbolMVias): Árbol para indexar registros por CI
            archivo_indice (str): Archivo para almacenar el índice de forma persistente
    '''
    
    def __init__(self, orden_arbol: int = 3, archivo_db: str = "estudiantes.dat", archivo_indice: str = "indice_ci.dat"):
        '''
            Inicializa el motor de indexación.
            
            Args:
                orden_arbol (int): Orden del árbol M-Vías (default: 3)
                archivo_db (str): Archivo de base de datos (default: "estudiantes.dat")
                archivo_indice (str): Archivo para almacenar el índice (default: "indice_ci.dat")
        '''
        self.db = RegistroEstudiante(archivo_db)
        self.arbol = ArbolMVias(orden_arbol)
        self.archivo_indice = archivo_indice
        
        # Cargar índice existente si existe
        if os.path.exists(archivo_indice):
            self.cargar_indice()

    def insertar(self, estudiante: dict) -> tuple:
        '''
            Inserta un nuevo estudiante en la base de datos y actualiza el índice.
            
            Args:
                estudiante (dict): Datos del estudiante
                
            Returns:
                tuple: (success, message)
        '''
        # Validar e insertar en la base de datos
        success, message = self.db.insertar(estudiante)
        if not success:
            return False, message
        
        # Obtener posición del último registro insertado
        registros = self.db.obtener_todos()
        posicion = len(registros) - 1  # Índice del nuevo registro
        
        # Actualizar árbol con la nueva CI
        ci = estudiante["CI"]
        self.arbol.insertar(ci, posicion)
        self.guardar_indice()
        
        return True, f"Estudiante {ci} insertado e indexado correctamente"

    def buscar(self, ci: str) -> dict:
        '''
            Busca un estudiante por CI usando el índice.
            
            Args:
                ci (str): Cédula de identidad a buscar
                
            Returns:
                dict: Datos del estudiante o None si no se encuentra
        '''
        # Buscar posición en el índice
        posicion = self.arbol.buscar(ci)
        if posicion is None:
            return None
        
        # Recuperar registro de la base de datos
        registros = self.db.obtener_todos()
        if 0 <= posicion < len(registros):
            return registros[posicion]
        return None

    def eliminar(self, ci: str) -> bool:
        '''
            Elimina un estudiante por CI usando el índice.
            
            Args:
                ci (str): Cédula de identidad a eliminar
                
            Returns:
                bool: True si se eliminó correctamente
        '''
        # Eliminar de la base de datos
        if not self.db.eliminar_por_ci(ci):
            return False
        
        # Eliminar del índice y actualizar
        self.arbol.eliminar(ci)
        self.guardar_indice()

        # Reindexar después de eliminar
        self.reindexar()
        return True

    def reindexar(self):
        '''
            Reconstruye completamente el índice desde la base de datos
        '''
        # Limpiar árbol existente
        self.arbol = ArbolMVias(self.arbol.get_orden())
        
        # Reconstruir índice desde la base de datos
        registros = self.db.obtener_todos()

        for idx, estudiante in enumerate(registros):
            ci = estudiante["CI"]
            self.arbol.insertar(ci, idx)
        self.guardar_indice()

    def guardar_indice(self):
        '''
            Guarda el índice en un archivo para persistencia
        '''
        with open(self.archivo_indice, 'w', encoding='utf-8') as f:
            # Guardar metadatos (orden del árbol)
            f.write(f"{self.arbol.get_orden()}\n")
            
            # Guardar pares (CI, posición) usando recorrido inorden
            for ci in self.arbol.inorden():
                posicion = self.arbol.buscar(ci)
                f.write(f"{ci},{posicion}\n")

    def cargar_indice(self):
        '''
            Carga el índice desde un archivo
        '''
        if not os.path.exists(self.archivo_indice):
            return
        
        with open(self.archivo_indice, 'r', encoding='utf-8') as f:
            # Leer orden del árbol (primera línea)
            orden = int(f.readline().strip())
            self.arbol = ArbolMVias(orden)
            
            # Leer pares (CI, posición)
            for line in f:
                ci, posicion = line.strip().split(',')
                self.arbol.insertar(ci, int(posicion))

    def __str__(self):
        '''
            Muestra información sobre el estado del motor
        '''
        num_registros = len(self.db.obtener_todos())
        num_indexados = len(self.arbol.inorden())
        return (
            f"Motor de Indexación\n"
            f"├── Registros en DB: {num_registros}\n"
            f"├── CIs indexados: {num_indexados}\n"
            f"└── Orden del árbol: {self.arbol.get_orden()}"
        )

    def imprimir_arbol(self):
        '''
            Muestra la estructura del árbol de indexación
        '''
        print("Estructura del Árbol de Indexación:")
        self.arbol.imprimir_arbol()