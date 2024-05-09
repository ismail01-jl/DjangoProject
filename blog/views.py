from django.shortcuts import render
from django.views.generic import ListView, DetailView , CreateView, UpdateView, DeleteView
from  .models import Post 
from django.urls import reverse_lazy
from blog.forms import PostForm
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = "posts"

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = "posts"


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog/post_list')
    form_class = PostForm

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    success_url = reverse_lazy('post_list')
    form_class = PostForm

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_produit.html'
    success_url = reverse_lazy('blog/post_list') 
    #form_class = PostForm