from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cuantos/', views.cuantos, name="cuantos"),
    path('listanombre/', views.lista_nombre, name="listanombre"),
    path('listatodos/', views.lista_todos, name="listatodos"),
    path('orderby/', views.orderby, name="orderby"),

]
