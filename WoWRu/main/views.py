from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Card
from .scripts import parse_card_xls_to_sql


def index(request):
    error = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            # if text == 'запарсить':
            #     parse_card_xls_to_sql(Card)
            return selected_cards(request, text)
        else:
            error = 'Данные введены некорректно'

    form = SearchForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/mainSearch.html', context)


def selected_cards(request, text):
    cards = Card.objects.all()
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
