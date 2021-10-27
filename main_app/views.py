from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

# Create your views here.
def home(request):
  return render(request, 'home.html')

def pokemon_index(request):
  pokemon = Pokemon.objects.all()
  return render(request, 'pokemon/index.html', { 'pokemon': pokemon })
  