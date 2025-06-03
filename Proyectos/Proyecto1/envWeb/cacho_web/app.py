from flask import Flask, render_template, request, jsonify, session
from models.Clase_Dados import Dados
from models.Clase_MCCTS import MCCTS
import random

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

@app.route('/')
def inicio():
    """Inicializa el juego con dados y estado inicial."""
    if 'dados' not in session:
        session['dados'] = [1, 1, 1, 1, 1]  # Dados iniciales
        session['turno'] = 'jugador'        # Empieza el jugador
        session['apuesta_jugador'] = None   # Apuesta del jugador (ej: 'PAR')
        session['apuesta_ia'] = None        # Apuesta de la IA
    return render_template('juego.html', 
                         dados=session['dados'],
                         turno=session['turno'])

@app.route('/apostar', methods=['POST'])
def apostar():
    """Recibe la apuesta del jugador y pasa turno a la IA."""
    apuesta = request.json.get('apuesta')
    session['apuesta_jugador'] = apuesta  # Ej: 'PAR', 'TRICA', etc.
    session['turno'] = 'ia'
    
    # La IA responde con su apuesta (simulada o usando MCTS)
    session['apuesta_ia'] = random.choice(['PAR', 'TRICA', 'ESCALERA'])
    
    return jsonify({
        'apuesta_ia': session['apuesta_ia'],
        'turno': session['turno']
    })

@app.route('/lanzar_dados', methods=['POST'])
def lanzar_dados():
    """Lanza los dados según el criterio (jugador o IA)."""
    dados_actuales = session.get('dados', [1, 1, 1, 1, 1])
    criterio = request.json.get('criterio', [1, 1, 1, 1, 1])  # Por defecto: lanzar todos
    
    # Lógica de lanzamiento
    nuevos_dados = [
        d if c == 0 else random.randint(1, 6) 
        for d, c in zip(dados_actuales, criterio)
    ]
    session['dados'] = nuevos_dados
    
    # Cambiar turno
    session['turno'] = 'ia' if session['turno'] == 'jugador' else 'jugador'
    
    return jsonify({
        'nuevos_dados': nuevos_dados,
        'turno': session['turno']
    })

@app.route('/turno_ia', methods=['POST'])
def turno_ia():
    """Ejecuta la jugada completa de la IA (apuesta + lanzamiento)."""
    if session.get('turno') != 'ia':
        return jsonify({'error': 'No es turno de la IA'}), 400
    
    # 1. La IA elige apuesta (usando MCTS o aleatorio)
    mccts = MCCTS()
    mccts.get_root().get_mano().set_dados(session['dados'])
    jugada, lanzada = mccts.search()  # Obtener mejor jugada y lanzamiento
    session['apuesta_ia'] = jugada.name
    
    # 2. Lanzar dados según la estrategia de la IA
    nuevos_dados = [
        d if l == 0 else random.randint(1, 6) 
        for d, l in zip(session['dados'], lanzada)
    ]
    session['dados'] = nuevos_dados
    session['turno'] = 'jugador'
    
    return jsonify({
        'apuesta_ia': session['apuesta_ia'],
        'lanzada': lanzada,
        'nuevos_dados': nuevos_dados,
        'turno': session['turno']
    })

if __name__ == '__main__':
    app.run(debug=True)