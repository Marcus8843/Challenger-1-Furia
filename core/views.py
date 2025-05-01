from django.shortcuts import render
from .models import Player, Match, Product

def home(request):
    players = Player.objects.all()
    matches = Match.objects.order_by('date')[:3]
    products = Product.objects.all()[:3]
    
    return render(request, 'core/home.html', {
        'players': players,
        'matches': matches,
        'products': products
    })