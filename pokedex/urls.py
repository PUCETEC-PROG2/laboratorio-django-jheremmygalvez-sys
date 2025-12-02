from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "pokedex"

router = routers.DefaultRouter()
router.register(r'pokemons', views.PokemonViewSet)
router.register(r'trainers', views.TrainerViewSet)

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon, name="pokemon"),
    path("trainer/<int:id>/", views.trainer, name="trainer"),
    path("create/", views.create, name="create"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:pokemon_id>/", views.delete_pokemon, name="delete_pokemon"),
    path("login/", views.CustomLoginView.as_view(), name="login"),

    # rutas de la API REST
    path("api/", include(router.urls)),
]