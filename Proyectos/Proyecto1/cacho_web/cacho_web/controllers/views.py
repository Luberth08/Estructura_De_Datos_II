from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
import json
from cacho_web.controllers.GameController import GameController
from cacho_web.models.Clase_Dados import Dados
from cacho_web.models.Clase_Jugada import Jugada


@never_cache
def inicio(request): 
    '''
        Vista que renderiza la pagina de inicio
        Parameters:
            request: Objeto HttpRequest que contiene la informacion de la peticion
        Returns:
            render: Renderiza la plantilla 'index.html'
    '''
    return render(request, 'index.html')    


@never_cache
def pre_game(request):
    '''
        Vista que renderiza la pagina de inicio del juego
        Parameters:
            request: Objeto HttpRequest que contiene la informacion de la peticion
        Returns:
            render: Renderiza la plantilla 'game.html'
    '''
    game = GameController()
    game.inicializar_juego()
    request.session['game'] = game.__dict__ 
    return render(request, 'game.html', {
        'turno': game.turno_actual,
        'dados': game.dados,
        'jugadores': game.jugadores
    })


@never_cache
def salir(request):
    '''
        Vista que cierra la sesion del usuario
        Parameters:
            request: Objeto HttpRequest que contiene la informacion de la peticion
        Returns:
            redirect: Redirige a la pagina de inicio
    '''
    logout(request)
    return redirect('/inicio/')


@never_cache
def lanzar_dados(request):
    '''
        Vista que lanza los dados y verifica la jugada
        Parameters:
            request: Objeto HttpRequest que contiene la informacion de la peticion
        Returns:
            JsonResponse: Respuesta en formato JSON con el resultado del lanzamiento
    '''
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    
    game = GameController()
    game.__dict__.update(request.session.get('game', {}))  # Recuperar estado
    criterio_lanzamiento = json.loads(request.POST.get('est_tiro'))
    jugada_apostada = Jugada(json.loads(request.POST.get('jugada')))
    if game.get_turno_actual() == 0:
        game.lanzar_dados_jugador(criterio_lanzamiento, jugada_apostada)
    elif game.get_turno_actual() == 1:
        game.lanzar_dados_ia()
    else:
        return JsonResponse({'error': 'Turno no válido'}, status=400)
    
    # Guardar estado
    request.session['game'] = game.__dict__  
    ult_jugada = Dados(game.get_dados()).obtener_jugada().value
    print(game.get_jugadores())
    return JsonResponse({
        'success': True,
        'dados': game.get_dados(),
        'jugadores': game.get_jugadores(),
        'turno': game.get_turno_actual(),
        'ult_jugada': ult_jugada,
    })