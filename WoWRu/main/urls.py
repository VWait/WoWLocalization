from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('selectedCards', views.selected_cards, name='selected'),
    path('advancedSearch', views.advanced_search, name='advanced'),
    path('card', views.card, name='card'),
    path('randomCard', views.random_card, name='random'),
    path('collection', views.collection_cards, name='collection')
]
