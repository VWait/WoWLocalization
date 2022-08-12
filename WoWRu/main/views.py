from django.shortcuts import render


def index(request):
    return render(request, 'main/mainSearch.html')


def selected_cards(request):
    return render(request, 'main/selectedCards.html')


def advanced_search(request):
    return render(request, 'main/advancedSearch.html')


def collection_cards(request):
    return render(request, 'main/collectionCards.html')


def random_card(request):
    # тут будет рандомайзер
    return render(request, 'main/card.html')


def card(request):
    return render(request, 'main/card.html')
