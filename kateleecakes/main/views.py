from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Торты', 'Кейки', 'зефир'],
        'obj': {
            'car':"BMW",
            'age':"29",
            'hobby': 'fitness'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')