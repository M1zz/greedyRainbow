from django.http import request
from django.shortcuts import render


# Create your views here.

def select_schedule(request):
    return render(request, 'greedyRainbow/index.html', {})
