from django.shortcuts import render
from django.http import JsonResponse
from .models import Pokemon

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PokemonSerializer

# Create your views here.
@api_view(['GET'])
def pokemonAPIRoute(request):
    api_urls = {
        'Pokemon List':'/pokemon/',
        'Pokemon Content': '/pokemon/<str:pk>'  
    }
    return Response(api_urls)

@api_view(['GET'])
def pokemonList(request):
    pokemon = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemon, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def pokemonContent(request, pk):
    pokemon = Pokemon.objects.get(id=pk)
    serializer = PokemonSerializer(pokemon, many=False)
    return Response(serializer.data)