from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'books'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # orders from newest to oldest


class PostDetailView(DetailView):
    model = Post
