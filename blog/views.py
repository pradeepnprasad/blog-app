from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class Blog_List_View(ListView):
    model = Post
    template_name = 'home.html'

class Blog_Detail_View(DetailView):
    model = Post
    template_name = 'post_detail.html'


class Blog_Create_View(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


class Blog_Update_View(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class Blog_Delete_View(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
