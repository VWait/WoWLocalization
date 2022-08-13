from django.shortcuts import render, redirect
from .forms import SearchForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selected')
        else:
            error = 'Данные введены некорректно'

    form = SearchForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/mainSearch.html', context)


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
