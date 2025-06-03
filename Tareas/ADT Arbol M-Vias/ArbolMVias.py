'''
    Title: Una clase que implementa los atributos y metodos de un arbol M-Vias
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 02/06/2025
    Version: 1.1
'''


from NodoMVias import NodoMVias


class ArbolMVias:
    '''
        Clase que representa un árbol m-vías.
        
        Atributos:
            m (int): Orden del árbol (máximo de hijos por nodo).
            raiz (NodoMVias): Nodo raíz del árbol.
    '''
    
    def __init__(self, m):
        '''
            Constructor del árbol M-Vías.
            
            Parámetros:
                m (int): Orden del árbol (debe ser al menos 3).
        '''
        if m < 3:
            raise ValueError("El orden del árbol (m) debe ser al menos 3")
        self.m = m
        self.raiz = None

    def esta_vacio(self):
        '''
            Verifica si el árbol está vacío.
            
            Retorna:
                bool: True si está vacío, False en caso contrario.
        '''
        return self.raiz is None

    def insertar(self, clave):
        '''
            Inserta una clave en el árbol. Maneja divisiones y actualiza la raíz.
            
            Parámetros:
                clave (int): Clave a insertar.
        '''
        if self.esta_vacio():
            self.raiz = NodoMVias(self.m)
            self.raiz.claves[0] = clave
            self.raiz.n = 1
            return

        # Insertar recursivamente y obtener posibles cambios por división
        nueva_raiz, clave_med, nuevo_hermano = self._insertar(self.raiz, clave)
        
        # Si hubo división en la raíz, crear una nueva raíz
        if clave_med is not None:
            nueva_raiz_padre = NodoMVias(self.m)
            nueva_raiz_padre.claves[0] = clave_med
            nueva_raiz_padre.n = 1
            nueva_raiz_padre.hijos[0] = nueva_raiz
            nueva_raiz_padre.hijos[1] = nuevo_hermano
            self.raiz = nueva_raiz_padre
        else:
            self.raiz = nueva_raiz

    def _insertar(self, nodo, clave):
        '''
            Método auxiliar recursivo para insertar una clave y manejar divisiones.
            
            Parámetros:
                nodo (NodoMVias): Nodo actual en la recursión.
                clave (int): Clave a insertar.
                
            Retorna:
                tuple: (nodo_actualizado, clave_mediana, nuevo_hermano)
                        - Si hay división: clave_mediana y nuevo_hermano no son None.
                        - Si no hay división: clave_mediana y nuevo_hermano son None.
        '''
        # Buscar posición para la clave en el nodo actual
        pos = 0
        while pos < nodo.n and clave > nodo.claves[pos]:
            pos += 1
            
        # Clave duplicada: no insertar
        if pos < nodo.n and clave == nodo.claves[pos]:
            return nodo, None, None
        
        # Caso base: nodo hoja o fin de recursión
        if nodo.es_hoja():
            if not nodo.esta_lleno(self.m):
                self._insertar_en_nodo(nodo, clave, pos, None)
                return nodo, None, None
            else:
                return self._dividir_nodo(nodo, clave, pos, None)
        else:
            # Insertar recursivamente en el hijo correspondiente
            hijo_actualizado, clave_med, nuevo_hermano = self._insertar(nodo.hijos[pos], clave)
            nodo.hijos[pos] = hijo_actualizado
            
            if clave_med is None:
                return nodo, None, None
            elif not nodo.esta_lleno(self.m):
                self._insertar_en_nodo(nodo, clave_med, pos, nuevo_hermano)
                return nodo, None, None
            else:
                return self._dividir_nodo(nodo, clave_med, pos, nuevo_hermano)

    def _insertar_en_nodo(self, nodo, clave, pos, nuevo_hermano):
        '''
            Inserta una clave en un nodo no lleno y ajusta los hijos.
            
            Parámetros:
                nodo (NodoMVias): Nodo donde se insertará la clave.
                clave (int): Clave a insertar.
                pos (int): Posición de inserción.
                nuevo_hermano (NodoMVias): Hijo derecho asociado a la clave (si existe).
        '''
        # Desplazar claves y hijos a la derecha desde la posición 'pos'
        for i in range(nodo.n, pos, -1):
            nodo.claves[i] = nodo.claves[i-1]
            
        for i in range(nodo.n + 1, pos, -1):
            nodo.hijos[i] = nodo.hijos[i-1]
            
        # Insertar clave y actualizar hijo derecho
        nodo.claves[pos] = clave
        nodo.hijos[pos+1] = nuevo_hermano
        nodo.n += 1

    def _dividir_nodo(self, nodo, clave, pos, nuevo_hermano):
        '''
            Divide un nodo lleno y calcula la clave mediana y el nuevo nodo hermano.
            
            Parámetros:
                nodo (NodoMVias): Nodo a dividir.
                clave (int): Clave nueva a insertar.
                pos (int): Posición donde se insertaría la clave.
                nuevo_hermano (NodoMVias): Hijo derecho asociado a la clave.
                
            Retorna:
                tuple: (nodo_izq, clave_mediana, nodo_der)
        '''
        # Crear listas temporales con claves e hijos actuales + nueva clave/hijo
        claves_tmp = []
        for i in range(nodo.n):
            claves_tmp.append(nodo.claves[i])
        claves_tmp.insert(pos, clave)
        
        hijos_tmp = []
        for i in range(len(nodo.hijos)):
            hijos_tmp.append(nodo.hijos[i])
        hijos_tmp.insert(pos+1, nuevo_hermano)
        
        # Calcular posición de la clave mediana
        medio = len(claves_tmp) // 2
        clave_mediana = claves_tmp[medio]
        
        # Crear nuevo nodo (hermano derecho)
        nuevo_nodo = NodoMVias(self.m)
        
        # Configurar nodo original (izquierdo) con claves/hijos antes de la mediana
        nodo.n = 0
        for i in range(medio):
            nodo.claves[i] = claves_tmp[i]
            nodo.n += 1
            
        for i in range(medio + 1):
            nodo.hijos[i] = hijos_tmp[i]
            if i > medio:
                nodo.hijos[i] = None
                
        # Configurar nuevo nodo (derecho) con claves/hijos después de la mediana
        j = 0
        for i in range(medio + 1, len(claves_tmp)):
            nuevo_nodo.claves[j] = claves_tmp[i]
            j += 1
            nuevo_nodo.n += 1
            
        j = 0
        for i in range(medio + 1, len(hijos_tmp)):
            nuevo_nodo.hijos[j] = hijos_tmp[i]
            j += 1
            
        return nodo, clave_mediana, nuevo_nodo

    def buscar(self, clave):
        '''
            Busca una clave en el árbol.
            
            Parámetros:
                clave (int): Clave a buscar.
                
            Retorna:
                bool: True si la clave existe, False en caso contrario.
        '''
        return self._buscar(self.raiz, clave)

    def _buscar(self, nodo, clave):
        '''
            Método auxiliar recursivo para buscar una clave.
            
            Parámetros:
                nodo (NodoMVias): Nodo actual en la recursión.
                clave (int): Clave a buscar.
                
            Retorna:
                bool: True si la clave existe, False en caso contrario.
        '''
        if nodo is None:
            return False
            
        pos = 0
        while pos < nodo.n and clave > nodo.claves[pos]:
            pos += 1
            
        if pos < nodo.n and clave == nodo.claves[pos]:
            return True
            
        if nodo.es_hoja():
            return False
            
        return self._buscar(nodo.hijos[pos], clave)

    def recorrido_inorden(self):
        '''
            Realiza un recorrido inorden (izquierda, raíz, derecha) del árbol.
            
            Retorna:
                list: Lista de claves en orden inorden.
        '''
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, resultado):
        """
        Método auxiliar recursivo para recorrido inorden.
        
        Parámetros:
            nodo (NodoMVias): Nodo actual.
            resultado (list): Lista para almacenar las claves.
        """
        if nodo is not None:
            for i in range(nodo.n):
                self._inorden(nodo.hijos[i], resultado)
                resultado.append(nodo.claves[i])
            self._inorden(nodo.hijos[nodo.n], resultado)

    def recorrido_preorden(self):
        '''
            Realiza un recorrido preorden (raíz, izquierda, derecha) del árbol.
            
            Retorna:
                list: Lista de claves en orden preorden.
        '''
        resultado = []
        self._preorden(self.raiz, resultado)
        return resultado

    def _preorden(self, nodo, resultado):
        '''
            Método auxiliar recursivo para recorrido preorden.
            
            Parámetros:
                nodo (NodoMVias): Nodo actual.
                resultado (list): Lista para almacenar las claves.
        '''
        if nodo is not None:
            for i in range(nodo.n):
                resultado.append(nodo.claves[i])
            for hijo in nodo.hijos:
                self._preorden(hijo, resultado)

    def recorrido_postorden(self):
        '''
            Realiza un recorrido postorden (izquierda, derecha, raíz) del árbol.
            
            Retorna:
                list: Lista de claves en orden postorden.
        '''
        resultado = []
        self._postorden(self.raiz, resultado)
        return resultado

    def _postorden(self, nodo, resultado):
        '''
            Método auxiliar recursivo para recorrido postorden.
            
            Parámetros:
                nodo (NodoMVias): Nodo actual.
                resultado (list): Lista para almacenar las claves.
        '''
        if nodo is not None:
            for hijo in nodo.hijos:
                self._postorden(hijo, resultado)
            for i in range(nodo.n):
                resultado.append(nodo.claves[i])

    def visualizar(self):
        '''
            Muestra el árbol m-vías de forma jerárquica en la consola.
            Cada nodo se muestra con sus claves, y se indentan los hijos para reflejar la estructura.
        '''
        if self.esta_vacio():
            print("Árbol vacío")
            return
        self._visualizar(self.raiz, 0)

    def _visualizar(self, nodo, nivel):
        '''
            Método auxiliar recursivo para visualizar el árbol.
            
            Parámetros:
                nodo (NodoMVias): Nodo actual.
                nivel (int): Nivel de profundidad (para indentación).
        '''
        if nodo is None:
            return
        
        # Imprimir claves del nodo actual con indentación según el nivel
        print("    " * nivel + "└─", end=" ")
        claves_str = [str(clave) if clave is not None else "None" for clave in nodo.get_claves()[:nodo.n]]
        print(f"Nodo({', '.join(claves_str)})")
        
        # Recorrer los hijos recursivamente
        for i in range(len(nodo.get_hijos())):
            self._visualizar(nodo.get_hijo(i), nivel + 1)
