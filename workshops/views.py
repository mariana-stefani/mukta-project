from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

events = [
    {
        'title': 'Meditation Workshop',
        'date': '26th September 2020',
        'location': 'Hyde Park - London',
        'time': '16:00',
        'instructor': 'Mariana Stefani',
        'content': 'Come and join us for a meditation workshop',
        'images': 'https://cdn.pixabay.com/photo/2016/11/02/11/08/meditation-1791113_1280.jpg',

    },
    {
        'title': 'Mantras Workshop',
        'date': '12th October 2020',
        'location': 'Regent\'s Park - London',
        'time': '14:00',
        'instructor': 'Mariana Stefani',
        'content': 'Come and join us for an afternoon singing mantras',
        'images': 'https://cdn.pixabay.com/photo/2020/05/08/13/33/lotus-5145730_1280.jpg',

    }
]


def workshops(request):
    context = {
        'events': events
    }
    return render(request, 'workshops/workshops.html', context)
