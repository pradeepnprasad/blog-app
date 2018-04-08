from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class Blog_List_View(ListView):
    model = Post
    template_name = 'home.html'

class Blog_Detail_View(DetailView):
    model = Post
    template_name = 'post_detail.html'