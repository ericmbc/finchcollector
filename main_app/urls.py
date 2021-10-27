from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('pokemon/', views.pokemon_index, name='index'),
  path('pokemon/<int:pokemon_id>/', views.pokemon_detail, name='detail'),
  path('pokemon/new', views.pokemon_new,),
  path('pokemon/submit', views.pokemon_create),
  path('pokemon/create/', views.PokemonCreate.as_view(), name='pokemon_create'),
  path('pokemon/<int:pokemon_id>/delete/', views.pokemon_delete),
  path('pokemon/<int:pokemon_id>/edit/', views.pokemon_edit),
  path('pokemon/<int:pokemon_id>/update/', views.pokemon_update),
]