from django.shortcuts import render, redirect
from .models import Pokemon
# from .forms import PokemonForm

# Create your views here.
def book(request):
    pokemons = Pokemon.objects.order_by('number')
    context = {
        'pokemons': pokemons,
    }
    return render(request, 'record/book.html', context)

# def create(request):
    # # POST면
    # if request.method == 'POST':
    #     pokemon_form = PokemonForm(request.POST)
    #     if pokemon_form.is_valid():
    #         pokemon_form.save()
    #         return redirect('record:book')
    # # GET이면
    # else:
    #     pokemon_form = PokemonForm()
    # return render(request, 'record/create.html', { 'pokemon_form': pokemon_form })

def create(request):
    pokemon = Pokemon()
    # POST
    if request.method == 'POST':
        try:
            pokemon.number = request.POST['number']
        except:
            pokemon.number = None
        try:
            pokemon.name = request.POST['name']
        except:
            pokemon.name = None
        try:
            pokemon.types = request.POST.getlist('types')
        except:
            pokemon.types = None
        try:
            pokemon.image = request.FILES['image']
        except:
            pokemon.image = None

        if pokemon.number != None and pokemon.name != None and pokemon.types != None:
            pokemon.save()
            return redirect('record:book')
    
    # GET
    type_list = {
        '노말': 'normal',
        '격투': 'fight',
        '바위': 'rock',
        '불꽃': 'flame',
        '독': 'poison',
        '고스트': 'ghost',
        '물': 'water',
        '땅': 'earth',
        '드래곤': 'dragon',
        '풀': 'grass',
        '비행': 'flight',
        '악': 'evil',
        '전기': 'electricity',
        '에스퍼': 'esper',
        '강철': 'steel',
        '얼음': 'ice',
        '벌레': 'bug',
        '페어리': 'fairy',
    }
    context = {
        'type_list': type_list,
        'pokemon': pokemon,
    }
    return render(request, 'record/create.html', context)

def delete(request, pk):
    Pokemon.objects.get(pk=pk).delete()
    return redirect('record:book')