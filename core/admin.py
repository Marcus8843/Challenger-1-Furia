from django.contrib import admin
from .models import Player, Match, Product

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'role', 'rating')

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('opponent', 'tournament', 'date')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')