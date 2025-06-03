from django import template
import json

register = template.Library()  # Objeto para registrar filtros

@register.filter(name='tojson')  # Decorador para definir el filtro
def tojson(value):
    """
    Convierte un objeto Python a JSON.
    Uso en template: {{ datos|tojson }}
    """
    return json.dumps(value)  # Serializa a JSON