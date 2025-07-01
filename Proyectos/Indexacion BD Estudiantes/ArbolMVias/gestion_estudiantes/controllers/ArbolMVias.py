'''
    Title: Una clase que implementa los atributos y metodos de un Arbol M-Vias para indexación de bases de datos.
    Author: Villarroel Gutierrez Josue Luberth 
    Date: 10/06/2025
    Version: 1.0
'''


from collections import deque
from .NodoMVias import NodoMVias


class ArbolMVias:
    '''
        Implementación de un árbol M-Vías de orden m donde se
        maneja operaciones de inserción, búsqueda y mantenimiento de propiedades.

        Atributos:
            orden (int): Orden del árbol (máximo de hijos por nodo)
            raiz (NodoMVias): Nodo raíz del árbol
    '''
    
    def __init__(self, orden: int):
        '''
            Inicializa el árbol con el orden especificado.
            
            Args:
                orden (int): Orden del árbol (máximo de hijos por nodo)
        '''
        if orden <= 2:
            raise ValueError("El orden del nodo debe ser al menos 3")

        self.__orden = orden              # Orden del árbol (m)
        self.__raiz = NodoMVias()         # Raíz del árbol
        
    # Métodos Getter y Setter para raiz
    def get_raiz(self):
        return self.__raiz
    
    def set_raiz(self, raiz : NodoMVias):
        self.__raiz = raiz
        
    def get_orden(self):
        return self.__orden

    # Funcion que devuelve el nodo hoja mas prometedor para insertar la nueva clave
    def __buscar_nodo(self, clave, nodo_actual: NodoMVias) -> NodoMVias:
        '''
            Devuelve el nodo hoja adecuado para insertar una nueva clave.
            
            Args:
                clave (any): Clave a insertar
                nodo_actual (NodoMVias): Nodo actual en el recorrido
                
            Returns:
                NodoMVias: Nodo hoja donde se debe insertar la clave
        '''
        if nodo_actual is None:
            return None
        
        # Caso base: nodo hoja
        if nodo_actual.get_es_hoja():
            return nodo_actual
        
        claves = [c[0] for c in nodo_actual.get_claves()]
        hijos = nodo_actual.get_hijos()
        
        if NodoMVias.criterio_orden(clave, claves[-1]) >= 0:
            return self.__buscar_nodo(clave, hijos[-1])
        
        # Búsqueda binaria
        i, j = 0, len(claves) - 1
        while i < j:
            k = (i + j) // 2
            if NodoMVias.criterio_orden(clave, claves[k]) == -1:
                j = k
            else:
                i = k + 1
        
        if i < len(hijos) and hijos[i] is not None:
            return self.__buscar_nodo(clave, hijos[i])
        
        return None
    
    # Metodo para insertar una clave en el arbol
    def insertar(self, clave, puntero=None):
        '''
            Inserta una nueva clave en el arbol.
            
            Args:
                clave (any): Clave a insertar
                puntero (any): Puntero asociado a la clave (por defecto None)
        '''
        # Buscar nodo hoja para inserción
        nodo_hoja = self.__buscar_nodo(clave, self.__raiz)
        if nodo_hoja is None:
            raise RuntimeError("No se pudo encontrar nodo hoja para inserción")
        
        # Insertar en el nodo hoja
        nodo_hoja.insertar(clave, puntero)
        
        # Verificar si necesita división
        if len(nodo_hoja.get_claves()) > self.__orden - 1:
            self.__dividir(nodo_hoja)

    # Metodo privado para dividir un nodo que ha excedido su capacidad
    def __dividir(self, nodo: NodoMVias):
        '''
            Divide un nodo que ha excedido su capacidad máxima.
            
            Args:
                nodo (NodoMVias): Nodo a dividir
        '''
        claves = nodo.get_claves()
        hijos = nodo.get_hijos()
        
        # Calcular la posición mediana
        medio = (self.__orden - 1) // 2 
        clave_mediana = claves[medio]
        
        # Crear nuevos nodos (izquierdo y derecho)
        nodo_izq = NodoMVias()
        nodo_der = NodoMVias()
        
        # Dividir claves
        nodo_izq.set_claves(claves[:medio])
        nodo_der.set_claves(claves[medio+1:])
        
        # Dividir hijos y actualizar estado de hoja
        if not nodo.get_es_hoja():
            nodo_izq.set_hijos(hijos[:medio+1])
            nodo_der.set_hijos(hijos[medio+1:])
            nodo_izq.set_es_hoja(False)
            nodo_der.set_es_hoja(False)
            
            # Actualizar padres de los hijos movidos
            for hijo in hijos[:medio+1]:
                hijo.set_padre(nodo_izq)
            for hijo in hijos[medio+1:]:
                hijo.set_padre(nodo_der)
        else:
            # Para hojas, crear listas de hijos None con tamaño correcto
            nodo_izq.set_hijos([None] * (len(claves[:medio]) + 1))
            nodo_der.set_hijos([None] * (len(claves[medio+1:]) + 1))
        
        # Manejar la clave mediana
        padre = nodo.get_padre()
        if padre is None:
            # Crear nueva raíz
            nueva_raiz = NodoMVias()
            nueva_raiz.insertar(clave_mediana[0], clave_mediana[1])
            nueva_raiz.set_es_hoja(False)
            nueva_raiz.set_hijos([nodo_izq, nodo_der])
            
            # Actualizar referencias de padres
            nodo_izq.set_padre(nueva_raiz) 
            nodo_der.set_padre(nueva_raiz)

            self.__raiz = nueva_raiz
        else:
            # Insertar clave mediana en el padre
            padre.insertar(clave_mediana[0], clave_mediana[1])
            
            # Reemplazar el nodo dividido por los dos nuevos nodos
            hijos_padre = padre.get_hijos()
            idx = hijos_padre.index(nodo)
            hijos_padre[idx] = nodo_izq
            hijos_padre[idx+1] = nodo_der
            
            # Actualizar padres
            nodo_izq.set_padre(padre)
            nodo_der.set_padre(padre)
            
            # Verificar si el padre necesita división
            if len(padre.get_claves()) > self.__orden - 1:
                self.__dividir(padre)

    # Método para buscar una clave en el árbol
    def buscar(self, clave):
        '''
            Busca una clave en el árbol y devuelve el puntero asociado si existe, None en caso contrario.

            Args:
                clave (any): Clave a buscar
        '''
        return self.__buscar_rec(self.__raiz, clave)
    
    def __buscar_rec(self, nodo_actual, clave):
        '''
            Método recursivo para buscar una clave en el árbol. 

            Args:
                nodo_actual (NodoMVias): Nodo actual en el recorrido
                clave (any): Clave a buscar
        '''
        if nodo_actual is None:
            return None
        
        claves = nodo_actual.get_claves()
        hijos = nodo_actual.get_hijos()
        
        # Buscar en las claves del nodo actual
        i, j = 0, len(claves) - 1
        while i < j:
            k = (i + j) // 2
            if NodoMVias.criterio_orden(clave, claves[k][0]) <= 0:
                j = k
            else:
                i = k + 1

        if i < len(claves):
            if NodoMVias.criterio_orden(clave, claves[i][0]) == 0:
                return claves[i][1]
            
            # Determinar por qué hijo continuar
            if NodoMVias.criterio_orden(clave, claves[i][0]) > 0:
                return self.__buscar_rec(hijos[i+1], clave)
            return self.__buscar_rec(hijos[i], clave)
        return None

    # Método de recorrido del árbol inorden
    def inorden(self):
        '''
            Realiza un recorrido inorden del árbol y devuelve las claves en orden ascendente.
        '''
        return self.__inorden_rec(self.__raiz)

    def __inorden_rec(self, nodo):
        '''
            Método recursivo para realizar un recorrido inorden del árbol.
        '''
        if nodo is None or len(nodo.get_claves()) == 0:
            return []
        
        result = []
        hijos = nodo.get_hijos()
        claves = nodo.get_claves()
        for i in range(len(claves)):
            if hijos[i] is not None:
                result += self.__inorden_rec(hijos[i])
            result.append(claves[i][0])
        if hijos[-1] is not None:
            result += self.__inorden_rec(hijos[-1])

        return result

    # Método de recorrido del árbol preorden 
    def preorden(self):
        '''
            Realiza un recorrido preorden del árbol e imprime las claves en el orden de inserción.
        '''
        return self.__preorden_rec(self.__raiz)

    def __preorden_rec(self, nodo):
        '''
            Método recursivo para realizar un recorrido preorden del árbol.
        '''
        if nodo is None or len(nodo.get_claves()) == 0:
            return
        
        result = []
        claves = nodo.get_claves()
        hijos = nodo.get_hijos()
        for clave in claves:
            result.append(clave[0])
        for hijo in hijos:
            if hijo is not None:
                result += self.__preorden_rec(hijo)

        return result

    # Método de recorrido del árbol postorden
    def postorden(self):
        '''
            Realiza un recorrido postorden del árbol y devuelve las claves en orden descendente.
        '''
        return self.__postorden_rec(self.__raiz)

    def __postorden_rec(self, nodo):
        '''
            Método recursivo para realizar un recorrido postorden del árbol.
        '''
        if nodo is None or len(nodo.get_claves()) == 0:
            return []
        
        result = []
        hijos = nodo.get_hijos()
        claves = nodo.get_claves()
        for hijo in hijos:
            if hijo is not None:
                result += self.__postorden_rec(hijo)
        for clave in claves:  
            result.append(clave[0])

        return result

    # Método para eliminar una clave del árbol
    def eliminar(self, clave):
        '''
            Elimina una clave del árbol.
            
            Args:
                clave (any): Clave a eliminar

            Returns:
                bool: True si la clave fue eliminada, False si no existe
        '''
        if self.__raiz is None or not self.__raiz.get_claves():
            return False 
            
        eliminado = self.__eliminar_rec(self.__raiz, clave)
        
        # Si la raíz quedó vacía
        if self.__raiz and self.__raiz.get_claves() == []:
            if self.__raiz.get_hijos() and self.__raiz.get_hijos()[0] is not None:
                self.__raiz = self.__raiz.get_hijos()[0]
                self.__raiz.set_padre(None)
            else:
                self.__raiz = None
                
        return eliminado

    # Método recursivo para eliminar una clave del árbol
    def __eliminar_rec(self, nodo, clave):
        '''
            Método recursivo para eliminar una clave del árbol.

            Args:
                nodo (NodoMVias): Nodo actual en el recorrido
                clave (any): Clave a eliminar
        '''
        if nodo is None:
            return False

        claves = nodo.get_claves()
        hijos = nodo.get_hijos()
        
        # Buscar la posición de la clave
        i, j = 0, len(claves) - 1
        while i < j:
            k = (i + j) // 2
            if NodoMVias.criterio_orden(clave, claves[k][0]) < 0:
                j = k
            else:
                i = k + 1

        # Caso 1: Clave encontrada en este nodo
        if i < len(claves) and NodoMVias.criterio_orden(clave, claves[i][0]) == 0:
            if nodo.get_es_hoja():
                self.__eliminar_de_hoja(nodo, i)
            else:
                self.__eliminar_de_interno(nodo, i)
            return True
        else:
            if nodo.get_es_hoja():
                return False
                
            # Continuar en el hijo correspondiente
            if NodoMVias.criterio_orden(clave, claves[i][0]) > 0:
                eliminado = self.__eliminar_rec(hijos[i+1], clave)
            else:
                eliminado = self.__eliminar_rec(hijos[i], clave)

            if eliminado:
                self.__rebalancear(nodo, i)
            return eliminado

    # Método privado para eliminar de hoja
    def __eliminar_de_hoja(self, nodo, idx):
        '''
            Elimina una clave de un nodo hoja.

            Args:
                nodo (NodoMVias): Nodo hoja del que se eliminará la clave
                idx (int): Índice de la clave a eliminar
        '''
        claves = nodo.get_claves()
        hijos = nodo.get_hijos()
        claves.pop(idx)
        
        if idx < len(hijos) - 1:
            hijos.pop(idx+1)
        else:
            hijos.pop()

    # Método privado para eliminar de un nodo interno
    def __eliminar_de_interno(self, nodo, idx):
        '''
            Elimina una clave de un nodo interno.

            Args:
                nodo (NodoMVias): Nodo interno del que se eliminará la clave
                idx (int): Índice de la clave a eliminar
        '''
        claves = nodo.get_claves()
        
        # Opción 1: Predecesor
        predecesor, nodo_predecesor = self.__obtener_predecesor(nodo, idx)
        if nodo_predecesor and len(nodo_predecesor.get_claves()) > self.__min_claves():
            claves[idx] = predecesor
            self.__eliminar_rec(nodo_predecesor, predecesor[0])
            return
        
        # Opción 2: Sucesor
        sucesor, nodo_sucesor = self.__obtener_sucesor(nodo, idx)
        if nodo_sucesor and len(nodo_sucesor.get_claves()) > self.__min_claves():
            claves[idx] = sucesor
            self.__eliminar_rec(nodo_sucesor, sucesor[0])
            return
        
        # Opción 3: Fusión
        self.__fusionar_hijos(nodo, idx)

    # Método privado para obtener el predecesor o sucesor
    def __obtener_predecesor(self, nodo, idx):
        '''
            Obtiene el predecesor de una clave en un nodo interno.

            Args:
                nodo (NodoMVias): Nodo interno del que se obtendrá el predecesor
                idx (int): Índice de la clave cuyo predecesor se busca
        '''
        actual = nodo.get_hijos()[idx]
        while not actual.get_es_hoja():
            actual = actual.get_hijos()[-1]
        return actual.get_claves()[-1], actual

    # Método privado para obtener el sucesor de una clave en un nodo interno
    def __obtener_sucesor(self, nodo, idx):
        '''
            Obtiene el sucesor de una clave en un nodo interno.

            Args:
                nodo (NodoMVias): Nodo interno del que se obtendrá el sucesor
                idx (int): Índice de la clave cuyo sucesor se busca
        '''
        actual = nodo.get_hijos()[idx+1]
        while not actual.get_es_hoja():
            actual = actual.get_hijos()[0]
        return actual.get_claves()[0], actual

    # Método privado para fusionar dos hijos de un nodo padre
    def __fusionar_hijos(self, padre, idx):
        '''
            Fusiona dos hijos de un nodo padre en uno nuevo.

            Args:
                padre (NodoMVias): Nodo padre de los hijos a fusionar
                idx (int): Índice del hijo izquierdo a fusionar con el derecho
        '''
        claves_padre = padre.get_claves()
        hijos_padre = padre.get_hijos()
        
        hijo_izq = hijos_padre[idx]
        hijo_der = hijos_padre[idx+1]
        clave_separadora = claves_padre[idx]
        
        # Crear nuevo nodo fusionado
        nuevas_claves = hijo_izq.get_claves() + [clave_separadora] + hijo_der.get_claves()
        nuevos_hijos = hijo_izq.get_hijos() + hijo_der.get_hijos()
        
        nuevo_nodo = NodoMVias()
        nuevo_nodo.set_claves(nuevas_claves)
        nuevo_nodo.set_hijos(nuevos_hijos)
        nuevo_nodo.set_es_hoja(hijo_izq.get_es_hoja())
        nuevo_nodo.set_padre(padre)
        
        # Actualizar padres de los hijos movidos
        for hijo in nuevos_hijos:
            if hijo:
                hijo.set_padre(nuevo_nodo)
        
        # Actualizar padre
        claves_padre.pop(idx)
        hijos_padre.pop(idx+1)
        hijos_padre[idx] = nuevo_nodo

    # Método privado para rebalancear un nodo después de una eliminación
    def __rebalancear(self, padre, idx_hijo):
        '''
            Rebalancea un nodo padre después de eliminar una clave de uno de sus hijos.

            Args:
                padre (NodoMVias): Nodo padre del hijo que necesita rebalanceo
                idx_hijo (int): Índice del hijo en el padre que necesita rebalanceo
        '''
        # Verificar que el hijo exista
        if idx_hijo >= len(padre.get_hijos()) or padre.get_hijos()[idx_hijo] is None:
            return
        
        hijo = padre.get_hijos()[idx_hijo]
        if len(hijo.get_claves()) >= self.__min_claves():
            return 
            
        # Intentar redistribución izquierda
        if idx_hijo > 0:
            hermano_izq = padre.get_hijos()[idx_hijo-1]
            if len(hermano_izq.get_claves()) > self.__min_claves():
                self.__redistribuir_izquierda(padre, idx_hijo-1, hermano_izq, hijo)
                return
                
        # Intentar redistribución derecha
        if idx_hijo < len(padre.get_hijos()) - 1:
            hermano_der = padre.get_hijos()[idx_hijo+1]
            if len(hermano_der.get_claves()) > self.__min_claves():
                self.__redistribuir_derecha(padre, idx_hijo, hijo, hermano_der)
                return
                
        # Fusión si no se pudo redistribuir
        if idx_hijo > 0:
            self.__fusionar_hijos(padre, idx_hijo-1)
        else:
            self.__fusionar_hijos(padre, idx_hijo)

    # Métodos privados para redistribuir claves entre nodos hermanos
    def __redistribuir_izquierda(self, padre, idx_hermano, hermano_izq, hijo):
        '''
            Redistribuye claves entre un nodo hijo y su hermano izquierdo.
            
            Args:
                padre (NodoMVias): Nodo padre de los nodos a redistribuir
                idx_hermano (int): Índice del hermano izquierdo en el padre
                hermano_izq (NodoMVias): Nodo hermano izquierdo
                hijo (NodoMVias): Nodo hijo al que se redistribuirá la clave
        '''
        claves_padre = padre.get_claves()
        claves_hermano = hermano_izq.get_claves()
        claves_hijo = hijo.get_claves()
        
        # Mover clave del padre al hijo
        clave_padre = claves_padre[idx_hermano]
        claves_hijo.insert(0, clave_padre)
        
        # Mover clave del hermano al padre
        clave_hermano = claves_hermano.pop()
        claves_padre[idx_hermano] = clave_hermano
        
        # Mover hijo del hermano al hijo
        if not hermano_izq.get_es_hoja():
            ultimo_hijo_hermano = hermano_izq.get_hijos().pop()
            hijo.get_hijos().insert(0, ultimo_hijo_hermano)
            if ultimo_hijo_hermano:
                ultimo_hijo_hermano.set_padre(hijo)

    def __redistribuir_derecha(self, padre, idx_hijo, hijo, hermano_der):
        '''
            Redistribuye claves entre un nodo hijo y su hermano derecho.

            Args:
                padre (NodoMVias): Nodo padre de los nodos a redistribuir
                idx_hijo (int): Índice del hijo en el padre
                hijo (NodoMVias): Nodo hijo al que se redistribuirá la clave
                hermano_der (NodoMVias): Nodo hermano derecho
        '''
        claves_padre = padre.get_claves()
        claves_hermano = hermano_der.get_claves()
        claves_hijo = hijo.get_claves()
        
        # Mover clave del padre al hijo
        clave_padre = claves_padre[idx_hijo]
        claves_hijo.append(clave_padre)
        
        # Mover clave del hermano al padre
        clave_hermano = claves_hermano.pop(0)
        claves_padre[idx_hijo] = clave_hermano
        
        # Mover hijo del hermano al hijo
        if not hermano_der.get_es_hoja():
            primer_hijo_hermano = hermano_der.get_hijos().pop(0)
            hijo.get_hijos().append(primer_hijo_hermano)
            if primer_hijo_hermano:
                primer_hijo_hermano.set_padre(hijo)

    # Método privado para calcular el número mínimo de claves en un nodo
    def __min_claves(self):
        '''
            Devuelve (m-1) // 2, donde m es el orden del árbol.
        '''
        return (self.__orden - 1) // 2

    # Método para imprimir el árbol de forma jerárquica
    def imprimir_arbol(self):
        '''
            Imprime el árbol nivel por nivel mostrando para cada nodo:
            - Claves
            - Hijos (representados por sus primeras claves o "[]" si son hojas)
            - Estado de hoja
            - Padre (solo la clave mediana del padre)
        '''
        if self.__raiz is None:
            print("Árbol vacío")
            return
            
        cola = deque()
        cola.append(self.__raiz)
        
        nivel_actual = 0
        while cola:
            n_nodos = len(cola)
            print(f"\n{'═'*50}")
            print(f" NIVEL {nivel_actual} ".center(50, '═'))
            
            for _ in range(n_nodos):
                nodo = cola.popleft()
                claves_keys = [clave[0] for clave in nodo.get_claves()]
                hijos = nodo.get_hijos()
                es_hoja = nodo.get_es_hoja()
                padre = nodo.get_padre()
                
                # Obtener representación del padre
                padre_repr = "[]"
                if padre:
                    padre_claves = [clave[0] for clave in padre.get_claves()]
                    padre_repr = f"[{padre_claves[0]}..{padre_claves[-1]}]" if padre_claves else "[]"
                
                # Formatear información de hijos
                hijos_info = []
                for hijo in hijos:
                    if hijo is None:
                        hijos_info.append("∅")
                    else:
                        hijo_claves = hijo.get_claves()
                        if hijo_claves:
                            hijo_keys = [clave[0] for clave in hijo_claves]
                            if len(hijo_keys) > 3:
                                hijos_info.append(f"[{hijo_keys[0]}..{hijo_keys[-1]}]")
                            else:
                                hijos_info.append(str(hijo_keys))
                        else:
                            hijos_info.append("∅")
                
                # Construir representación del nodo
                print("\n" + "─"*50)
                print(f"Claves: {claves_keys}")
                print(f"Es hoja: {es_hoja}")
                print(f"Padre: {padre_repr}")
                print(f"Hijos ({len(hijos)}): {', '.join(hijos_info)}")
                
                # Agregar hijos no nulos a la cola
                if not es_hoja:
                    for hijo in hijos:
                        if hijo is not None:
                            cola.append(hijo)
            
            nivel_actual += 1
        print("\n" + "═"*50)

    def obtener_estructura(self):
        '''
            Devuelve una representación estructurada del árbol para visualización web
        '''
        if self.__raiz is None:
            return []
            
        estructura = []
        cola = deque()
        cola.append((self.__raiz, 0, None, 0))  # (nodo, nivel, padre, indice en padre)
        
        while cola:
            nodo, nivel, padre, indice_padre = cola.popleft()
            claves = [clave[0] for clave in nodo.get_claves()]
            hijos = nodo.get_hijos()
            
            padre_claves = []
            if padre is not None:
                padre_claves = [clave[0] for clave in padre.get_claves()]  
            
            nodo_info = {
                "nivel": nivel,
                "claves": claves,
                "es_hoja": nodo.get_es_hoja(),
                "num_hijos": len(hijos),
                "padre": padre_claves if padre else "Raíz",  
                "indice_padre": indice_padre,
                "hijos": []
            }
            
            # Agregar a la estructura
            if nivel >= len(estructura):
                estructura.append([])
            estructura[nivel].append(nodo_info)
            
            # Agregar hijos a la cola
            if not nodo.get_es_hoja():
                for i, hijo in enumerate(hijos):
                    if hijo is not None:
                        cola.append((hijo, nivel + 1, nodo, i))
        
        return estructura