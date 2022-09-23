from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

posts = [
    {
        'author': 'Norman',
        'title': 'Jack and the bean stalk',
        'date_published': '23-01-2022',
        'content': 'The anakim'
    },
    {
        'author': 'Peter',
        'title': 'Pat and the bean stalk',
        'date_published': '23-01-2022',
        'content': 'The Emim'

    },
    {
        'author': 'Mackay',
        'title': 'Mackay and the bean stalk',
        'date_published': '23-01-2022',
        'content': 'The Rephaim'

    }
]



def home(request):
    context = {
        'posts': posts,
        'title': 'books'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
