from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from oauth2_provider.contrib.rest_framework import TokenHasScope, OAuth2Authentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import Pokemon, Trainer
from .serializers import PokemonSerializer, TrainerSerializer

from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm


def index(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    template = loader.get_template('index.html')
    context = {
        'pokemons': pokemons,
        'trainers': trainers,
    }   
    return HttpResponse(template.render(context, request))


def pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    template = loader.get_template('display_pokemon.html')
    context = {'pokemon': pokemon}
    return HttpResponse(template.render(context, request))


def trainer(request, id):
    trainer = Trainer.objects.get(id=id)
    template = loader.get_template('display_trainer.html')
    context = {'trainer': trainer}
    return HttpResponse(template.render(context, request))

@login_required
def create(request):
    if request.method == "POST":
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')  
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def create_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')  
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:pokemon', id=pokemon_id)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form, 'pokemon': pokemon})


@login_required
def delete_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def edit_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainer', id=trainer_id)
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form, 'trainer': trainer})

@login_required
def delete_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    trainer.delete()
    return redirect('pokedex:index')

class CustomLoginView(LoginView):
    template_name = 'login_form.html'

    

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer