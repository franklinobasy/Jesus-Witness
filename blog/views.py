from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

class BlogView(TemplateView):
    template_name = "blog/posts.html"

class PostView(TemplateView):
    template_name = "blog/post.html"