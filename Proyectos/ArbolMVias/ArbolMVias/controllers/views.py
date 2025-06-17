from django.shortcuts import render, redirect
from ..models import RegistroForm
from ..Models.BD import MotorIndexacion
from ..settings import DATOS_DB

def index(request):
    # Obtener estructura del árbol
    motor = MotorIndexacion(DATOS_DB)
    arbol_estructura = motor._MotorIndexacion__arbol.obtener_estructura()
    
    context = {
        'arbol_estructura': arbol_estructura
    }
    return render(request, 'index.html', context)

def ver_arbol(request):
    """Vista dedicada para ver el árbol completo"""
    motor = MotorIndexacion(DATOS_DB)
    arbol_estructura = motor._MotorIndexacion__arbol.obtener_estructura()
    
    # Calcular total de nodos
    total_nodos = 0
    for nivel in arbol_estructura:
        total_nodos += len(nivel)
    
    context = {
        'arbol_estructura': arbol_estructura,
        'orden_arbol': motor._MotorIndexacion__arbol.get_orden(),
        'total_nodos': total_nodos,
        'detallado': True
    }
    return render(request, 'arbol.html', context)

def insertar_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            try:
                motor = MotorIndexacion(DATOS_DB)
                motor.insertar_registro(
                    form.cleaned_data['id_reg'],
                    form.cleaned_data['nombre'],
                    form.cleaned_data['email'],
                    form.cleaned_data['telefono']
                )
                return redirect('index')
            except Exception as e:
                return render(request, 'insertar.html', {
                    'form': form,
                    'error': f"Error: {str(e)}"
                })
    else:
        form = RegistroForm()
    return render(request, 'insertar.html', {'form': form})

def buscar_registro(request):
    if request.method == 'POST':
        id_reg = request.POST.get('id_reg')
        if id_reg:
            try:
                motor = MotorIndexacion(DATOS_DB)
                registro = motor.buscar_registro(int(id_reg))
                if registro:
                    return render(request, 'resultado.html', {
                        'registro': registro
                    })
                return render(request, 'buscar.html', {
                    'error': 'Registro no encontrado'
                })
            except ValueError:
                return render(request, 'buscar.html', {
                    'error': 'ID debe ser un número entero'
                })
    return render(request, 'buscar.html')

def eliminar_registro(request):
    if request.method == 'POST':
        id_reg = request.POST.get('id_reg')
        if id_reg:
            try:
                motor = MotorIndexacion(DATOS_DB)
                if motor.eliminar_registro(int(id_reg)):
                    return redirect('index')
                return render(request, 'index.html', {
                    'error': 'Registro no encontrado'
                })
            except ValueError:
                return render(request, 'index.html', {
                    'error': 'ID debe ser un número entero'
                })
    return redirect('index')