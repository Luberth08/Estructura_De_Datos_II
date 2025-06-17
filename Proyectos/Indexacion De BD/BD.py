import struct
from ArbolMVias import ArbolMVias

class MotorIndexacion:
    FORMATO_REGISTRO = "i50s50s15s"  # Sin espacios entre campos
    TAMANO_REGISTRO = struct.calcsize(FORMATO_REGISTRO)  # 4 + 50 + 50 + 15 = 119 bytes
    
    def __init__(self, nombre_archivo: str, orden_arbol: int = 5):
        self.__nombre_archivo = nombre_archivo
        self.__arbol = ArbolMVias(orden_arbol)
        self.__archivo = None
        self.__abrir_archivo()
        self.__reconstruir_indice()  # ¡Ahora funciona correctamente!

    def get_arbol(self):
        """Devuelve el árbol de índices"""
        return self.__arbol

    def __abrir_archivo(self):
        try:
            self.__archivo = open(self.__nombre_archivo, 'r+b')
        except FileNotFoundError:
            self.__archivo = open(self.__nombre_archivo, 'w+b')

    def __reconstruir_indice(self):
        """CORRECCIÓN: Reconstruye el índice correctamente"""
        self.__archivo.seek(0)
        while True:
            posicion = self.__archivo.tell()  # Guardar posición INICIAL del registro
            registro = self.__archivo.read(self.TAMANO_REGISTRO)
            
            if not registro or len(registro) < self.TAMANO_REGISTRO:
                break
                
            # Desempaqueta solo el ID (primer campo)
            id_reg = struct.unpack(self.FORMATO_REGISTRO, registro)[0]
            self.__arbol.insertar(id_reg, posicion)

    def insertar_registro(self, id_reg: int, nombre: str, email: str, telefono: str):
        """Inserta un registro estructurado en la base de datos"""
        # Verificar si el ID ya existe
        if self.__buscar_por_id(id_reg):  # Nueva función auxiliar
            raise ValueError(f"ID duplicado: {id_reg}")
        # Validar longitud de campos
        if len(nombre) > 50:
            raise ValueError("Nombre excede 50 caracteres")
        if len(email) > 50:
            raise ValueError("Email excede 50 caracteres")
        if len(telefono) > 15:
            raise ValueError("Teléfono excede 15 caracteres")
        
        # Eliminar registro existente si existe
        if self.__arbol.buscar(id_reg) not in [None, False]:
            self.__arbol.eliminar(id_reg)
        
        # Empaquetar datos en formato binario
        registro = struct.pack(
            self.FORMATO_REGISTRO,
            id_reg,
            nombre.encode('utf-8'),
            email.encode('utf-8'),
            telefono.encode('utf-8')
        )
        
        # Escribir al final del archivo
        self.__archivo.seek(0, 2)
        posicion = self.__archivo.tell()
        self.__archivo.write(registro)
        self.__archivo.flush()
        
        # Actualizar índice
        self.__arbol.insertar(id_reg, posicion)
    
    def __buscar_por_id(self, id_reg: int) -> bool:
        self.__archivo.seek(0)
        while True:
            pos = self.__archivo.tell()
            registro = self.__archivo.read(self.TAMANO_REGISTRO)
            if not registro:
                return False
            id_actual = struct.unpack(self.FORMATO_REGISTRO, registro)[0]
            if id_actual == id_reg:
                return True

    def buscar_registro(self, id_reg: int) -> dict:
        posicion = self.__arbol.buscar(id_reg)
        if posicion is None or posicion is False:
            return None
        
        self.__archivo.seek(posicion)
        registro = self.__archivo.read(self.TAMANO_REGISTRO)
        
        if not registro:
            return None
            
        # CORRECCIÓN: Desempaqueta todos los campos
        campos = struct.unpack(self.FORMATO_REGISTRO, registro)
        return {
            'id': campos[0],
            'nombre': campos[1].decode('utf-8').rstrip('\x00'),
            'email': campos[2].decode('utf-8').rstrip('\x00'),
            'telefono': campos[3].decode('utf-8').rstrip('\x00')
        }

    def eliminar_registro(self, id_reg: int) -> bool:
        """Elimina un registro del índice (marca como eliminado)"""
        return self.__arbol.eliminar(id_reg)

    def cerrar(self):
        """Cierra el archivo de datos"""
        if self.__archivo:
            self.__archivo.close()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cerrar()

    def debug_mostrar_archivo(self):
        """Muestra el contenido crudo del archivo para depuración"""
        self.__archivo.seek(0)
        position = 0
        print("\nDEBUG: CONTENIDO DEL ARCHIVO")
        while True:
            data = self.__archivo.read(self.TAMANO_REGISTRO)
            if not data: 
                break
            print(f"Pos {position}: {data}")
            position += self.TAMANO_REGISTRO