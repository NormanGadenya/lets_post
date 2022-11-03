from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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


class PostCreateView(LoginRequiredMixin, CreateView):
    # inorder to require the user to login before creating  a post
    # and the LoginRequired.. has to be at the end
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to the current logged in user before validating form
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    # inorder to require the user to login before creating  a post
    # and the LoginRequired.. has to be at the end
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # set the author to the current logged in user before validating form
        return super().form_valid(form)
