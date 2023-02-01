from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
def home(request):
    return render(request, 'home.html')

def testing(request):
    print("button worked")
    r = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
    data = json.loads(r.content)
    print(r.status_code)
    print(data['name'])
    return render(request, 'home.html')

