from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import Pokemon

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', { 'pokemon': pokemon })
  
def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  print(pokemon)
  return render(request, 'pokemon/detail.html', { 'pokemon': pokemon })

def pokemon_new(request):
  return render(request, 'pokemon/new.html')

def pokemon_create(request):
  pokemon = Pokemon.objects.create(
    name= request.POST['name'],
    breed= request.POST['breed'],
    description = request.POST['description'],
    age = request.POST['age']
  )
  return redirect(f'/pokemon/{pokemon.id}')

def pokemon_delete(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  pokemon.delete()
  return redirect('/pokemon')

def pokemon_edit(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  return render(request, 'pokemon/edit.html', {'pokemon': pokemon })

def pokemon_update(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  pokemon.name = request.POST['name']
  pokemon.breed = request.POST['breed']
  pokemon.description = request.POST['description']
  pokemon.age = request.POST['age']
  pokemon.save()
  return redirect(f'/pokemon/{pokemon.id}')
