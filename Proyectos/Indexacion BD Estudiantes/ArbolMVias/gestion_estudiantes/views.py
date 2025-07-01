from django.shortcuts import render, redirect
from django.http import HttpResponse
from .controllers.MotorIndexacion import MotorIndexacion
import os

# Inicializar el motor de indexación
MOTOR = MotorIndexacion(orden_arbol=5)

# Cargar datos existentes si hay
if os.path.exists("estudiantes.dat") and os.path.exists("indice_ci.dat"):
    try:
        MOTOR.cargar_indice()
    except:
        pass

def index(request):
    return render(request, 'index.html', {'total_estudiantes': len(MOTOR.db.obtener_todos()), 'total_indexados': len(MOTOR.arbol.inorden())})

def insertar_estudiante(request):
    mensaje = None
    if request.method == 'POST':
        ci = request.POST.get('ci')
        nombre = request.POST.get('nombre')
        apellido_paterno = request.POST.get('apellido_paterno')
        apellido_materno = request.POST.get('apellido_materno')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        ppa = request.POST.get('ppa')
        
        estudiante = {
            "CI": ci,
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "telefono": telefono,
            "email": email,
            "ppa": ppa
        }
        
        success, msg = MOTOR.insertar(estudiante)
        mensaje = {'texto': msg, 'tipo': 'success' if success else 'danger'}
    
    return render(request, 'insertar.html', {'mensaje': mensaje})

def buscar_estudiante(request):
    estudiante = None
    mensaje = None
    if request.method == 'POST':
        ci = request.POST.get('ci')
        estudiante = MOTOR.buscar(ci)
        if not estudiante:
            mensaje = {'texto': f'Estudiante con CI {ci} no encontrado', 'tipo': 'warning'}
    
    return render(request, 'buscar.html', {
        'estudiante': estudiante,
        'mensaje': mensaje
    })

def eliminar_estudiante(request):
    mensaje = None
    if request.method == 'POST':
        ci = request.POST.get('ci')
        if MOTOR.eliminar(ci):
            mensaje = {'texto': f'Estudiante con CI {ci} eliminado correctamente', 'tipo': 'success'}
        else:
            mensaje = {'texto': f'No se pudo eliminar el estudiante con CI {ci}', 'tipo': 'danger'}
    
    return render(request, 'eliminar.html', {'mensaje': mensaje})

def ver_arbol(request):
    # Obtener representación del árbol
    estructura = MOTOR.arbol.obtener_estructura()
    # Obtener estadísticas
    total_estudiantes = len(MOTOR.db.obtener_todos())
    total_indexados = len(MOTOR.arbol.inorden())
    
    return render(request, 'arbol.html', {
        'estructura': estructura,
        'total_estudiantes': total_estudiantes,
        'total_indexados': total_indexados,
        'orden_arbol': MOTOR.arbol.get_orden()
    })