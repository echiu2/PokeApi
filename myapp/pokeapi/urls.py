from django.urls import include, path
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.pokemonAPIRoute, name='view-pokemon-route'),
    path('pokemon-list/', views.pokemonList, name='pokemon-list'),
    path('pokemon-list/<str:pk>/', views.pokemonContent, name='pokemon-content')
]