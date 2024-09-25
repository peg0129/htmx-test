from django.urls import path
from . import views

urlpatterns = [
    path('', views.test),
    path('list/', views.pokemonList, name='list'),
    path('detail/<str:pokemon>/', views.pokemonDetail, name='detail'),
]