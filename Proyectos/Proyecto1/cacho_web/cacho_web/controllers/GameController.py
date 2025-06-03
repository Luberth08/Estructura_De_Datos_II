import random
from cacho_web.models.Clase_Dados import Dados
from cacho_web.models.Clase_MCTS_Cacho import MCCTS
from cacho_web.models.Clase_NodoD import NodeD
from cacho_web.models.Clase_Jugada import Jugada

class GameController:
    '''
        Clase que controla el flujo del juego de Cacho entre un jugador humano y una IA.
        
        Attributes:
            jugadores (list): Lista de jugadores en el juego.
            dados (list): Lista de valores de los dados.
            turno_actual (int): Índice del jugador cuyo turno es actualmente.
    '''     
    def __init__(self):
        '''
            Metodo constructor de la clase
        '''
        self.jugadores = []
        self.dados = [1, 1, 1, 1, 1]
        self.turno_actual = 0

    # Metodos getter y setter para 'jugadores'
    def get_jugadores(self):    
        '''Devuelve la lista de jugadores'''
        return self.jugadores
    
    def set_jugadores(self, jugadores: list):
        '''Establece la lista de jugadores'''  
        if len(jugadores) != 2:
            return
        self.jugadores = jugadores 

    # Metodos getter y setter para 'dados'
    def get_dados(self):
        '''Devuelve el valor de los dados'''
        return self.dados
    
    def set_dados(self, dados: list):
        '''Establece el valor de los dados'''  
        if len(dados) != 5:
            return
        for d in dados:
            if d not in [1,2,3,4,5,6]:
                return
        self.dados = dados
    
    # Metodos getter y setter para 'turno_actual'
    def get_turno_actual(self):
        '''Devuelve el indice del jugador cuyo turno es actualmente'''
        return self.turno_actual
    
    def set_turno_actual(self, turno_actual: int):
        '''Establece el indice del jugador cuyo turno es actualmente'''  
        if turno_actual < 0 or turno_actual > 1:
            return
        self.turno_actual = turno_actual
    
    # Metodo que inicializa el juego
    def inicializar_juego(self):
        self.jugadores = [
            {"nombre": "Jugador", "puntos": 0, "libreta": [], "tiros": 2},
            {"nombre": "IA", "puntos": 0, "libreta": [], "tiros": 2}
        ]
        self.turno_actual = random.randint(0, 1)

    # Metodo que lanza los dados del jugador humano
    def lanzar_dados_jugador(self, criterio_lanzamiento, jugada_apostada):
        '''
            Lanza los dados del jugador humano según el criterio de lanzamiento proporcionado.
            
            Parameters:
                criterio_lanzamiento (list): Lista de 5 elementos (unos y ceros) que indica 
                qué dados lanzar y cuáles no.
                jugada_apostada (int): La jugada que el jugador ha apostado.
        '''
        dados = Dados(self.dados)
        dados.lanzar(criterio_lanzamiento)
        self.dados = dados.get_dados()
        self.jugadores[0]['tiros'] -= 1
        self.statemachine(jugada_apostada)

    # Metodo que lanza los dados de la IA
    def lanzar_dados_ia(self):
        '''
            Realiza el turno de la IA, eligiendo una jugada y lanzando los dados.
            
            Returns:
                jugada (Jugada): La jugada elegida por la IA.
                lanzada (list): El criterio de lanzamiento elegido por la IA.
        '''
        dados = Dados(self.dados)
        if self.jugadores[1]['tiros'] == 2:
            dados.lanzar()
            self.jugadores[1]['tiros'] -= 1
            self.statemachine(Jugada.NONE)
        elif self.jugadores[1]['tiros'] == 1:
            mccts = MCCTS(i=10000, c=1.4)
            mccts.set_root(NodeD(mano=dados))
            for jugada_bloqueada in self.jugadores[1]['libreta']:
                mccts.bloquear_jugada(Jugada(jugada_bloqueada))
            jugada, lanzada = mccts.search()
            dados.lanzar(lanzada)
            self.jugadores[1]['tiros'] -= 1
            self.statemachine(jugada)
            mccts.imprimir_arbol()
            print(f"La IA decidio apostar a:{jugada}, lanzando los dados: {lanzada}")

    # Metodo que controla el flujo del juego entre el jugador humano y la IA
    def statemachine(self, jugada_apostada):
        '''
            Controla el flujo del juego entre el jugador humano y la IA.

            Parameters:
                jugada_apostada (int): La jugada que el jugador ha apostado.
        '''
        dados = Dados(self.dados)
        puntaje = 0
        jugada_obtenida = dados.obtener_jugada()
        sw_turno = False

        if self.jugadores[self.turno_actual]['tiros'] == 0: # Segundo tiro
            if jugada_obtenida == jugada_apostada:
                puntaje = dados.obtener_puntos()
            self.jugadores[self.turno_actual]['libreta'].append(jugada_apostada.value)
            sw_turno = True
        elif self.jugadores[self.turno_actual]['tiros'] == 1: # Primer Tiro
            if jugada_obtenida != Jugada.NONE and jugada_obtenida.value not in self.jugadores[self.turno_actual]['libreta']:
                puntaje = dados.obtener_puntos() + 5
                self.jugadores[self.turno_actual]['libreta'].append(jugada_obtenida.value)
                sw_turno = True

        self.jugadores[self.turno_actual]['puntos'] += puntaje
        if sw_turno:
            self.cambiar_turno()

    # Metodo que cambia el turno al siguiente jugador
    def cambiar_turno(self):
        '''
            Cambia el turno al siguiente jugador.
        '''
        self.jugadores[self.turno_actual]['tiros'] = 2
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)