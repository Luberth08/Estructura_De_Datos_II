'''
    Title: Una clase que implementa los atributos y metodos de una base de datos.
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 29/06/2025
    Version: 1.0
'''

import os
import csv
import re
from typing import Dict, List, Optional, Tuple

class RegistroEstudiante:
    '''
        Clase que gestiona una base de datos de estudiantes en un archivo CSV.

        Atributos:
            archivo: Nombre del archivo de datos.
            campos: Lista de campos de cada registro.
    '''
    
    def __init__(self, archivo: str = "estudiantes.dat"):
        '''
            Inicializa la base de datos. Crea el archivo si no existe.
            
            Args:
                archivo (str): Nombre del archivo de datos (default: "estudiantes.dat")
        '''
        self.archivo = archivo
        self.campos = [
            "CI", 
            "nombre", 
            "apellido_paterno", 
            "apellido_materno", 
            "telefono", 
            "email", 
            "ppa"
        ]
        
        # Crear archivo con cabecera si no existe
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()

    def __validar_campos(self, estudiante: Dict[str, str]) -> Tuple[bool, str]:
        '''
            Valida los campos del estudiante según reglas básicas.
            
            Args:
                estudiante (dict): Diccionario con los datos del estudiante.
                
            Returns:
                tuple: (bool, str) -> (True, "") si es válido, (False, mensaje_error) si no.
        '''
        if not all(campo in estudiante for campo in self.campos):
            return False, "Faltan campos obligatorios"
            
        if any(not estudiante[campo] for campo in self.campos):
            return False, "Todos los campos deben tener valores"
            
        if not re.match(r'^\d{1,10}$', estudiante["CI"]):
            return False, "CI debe contener solo números (1-10 dígitos)"
            
        if not re.match(r'^[\d\s\-]+$', estudiante["telefono"]):
            return False, "Teléfono solo puede contener números, espacios o guiones"
            
        if not re.match(r'^[^@]+@[^@]+\.[^@]+$', estudiante["email"]):
            return False, "Email no tiene formato válido"
            
        try:
            ppa = float(estudiante["ppa"])
            if not 0 <= ppa <= 100:
                return False, "PPA debe estar entre 0 y 100"
        except ValueError:
            return False, "PPA debe ser un número"
            
        return True, ""

    def insertar(self, estudiante: Dict[str, str]) -> Tuple[bool, str]:
        '''
            Inserta un nuevo registro de estudiante.
            
            Args:
                estudiante (dict): Diccionario con los campos del estudiante.
            
            Returns:
                bool: True si se insertó correctamente.
        '''
        # Validar campos requeridos
        valido, mensaje = self.__validar_campos(estudiante)
        if not valido:
            return False, mensaje
        
        # Verificar si CI ya existe
        if self.buscar_por_ci(estudiante["CI"]):
            return False, "El CI ya está registrado"

        with open(self.archivo, 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writerow(estudiante)
        return True, ""

    def buscar_por_ci(self, ci: str) -> Optional[Dict[str, str]]:
        '''
            Busca un estudiante por su CI.
            
            Args:
                ci (str): Cédula de identidad a buscar.
            
            Returns:
                dict: Datos del estudiante si existe, None si no se encuentra.
        '''
        with open(self.archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                if fila["CI"] == ci:
                    return fila
        return None

    def eliminar_por_ci(self, ci: str) -> bool:
        '''
            Elimina un estudiante por su CI (marca como eliminado).
            
            Args:
                ci (str): Cédula de identidad a eliminar.
            
            Returns:
                bool: True si se encontró y eliminó el registro.
        '''
        registros = []
        encontrado = False
        
        # Leer todos los registros
        with open(self.archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            registros = list(reader)
        
        # Filtrar el registro a eliminar
        nuevos_registros = [r for r in registros if r["CI"] != ci]
        encontrado = len(registros) != len(nuevos_registros)
        
        # Reescribir archivo si hubo cambios
        if encontrado:
            with open(self.archivo, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()
                writer.writerows(nuevos_registros)
        
        return encontrado

    def obtener_todos(self) -> List[Dict[str, str]]:
        '''
            Devuelve todos los registros de estudiantes.
            
            Returns:
                list: Lista de diccionarios con los estudiantes.
        '''
        with open(self.archivo, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)

    def __str__(self):
        '''
            Representación de los primeros 5 registros para depuración.
        '''
        registros = self.obtener_todos()
        total = len(registros)
        muestra = registros[:5] if total > 5 else registros
        return f"Registros: {total}\nMuestra: {muestra}"