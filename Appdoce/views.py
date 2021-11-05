from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
# Create your views here.


def index(request):
    return HttpResponse('Bienvenidos a Django!')


def cuantos(request):
    yes = Person.objects.filter(first_name__contains='luis').count()
    contexto = {
        'perso': yes
    }
    return render(request, 'cuantos.html', contexto)



def lista_nombre(request):
    #persona = Person.objects.all()
    persona = Person.objects.filter(first_name__contains='luis')
    contexto = {
        'perso': persona
    }
    return render(request, 'index.html', contexto)


def lista_todos(request):
    persona = Person.objects.all()
    contexto = {
        'perso': persona
    }
    return render(request, 'todos.html', contexto)


def orderby(request):
    persona = Person.objects.order_by('first_name')
    contexto = {
        'perso': persona
    }
    #https://docs.djangoproject.com/en/dev/ref/models/querysets/#order-by
    return render(request, 'orderby.html', contexto)
