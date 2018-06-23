from django.template import Library
from hotel.models import Ciudad

register = Library()

@register.simple_tag()
def lista_ciudades():
    return Ciudad.objects.all()
