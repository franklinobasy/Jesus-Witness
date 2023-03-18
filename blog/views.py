from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

# from blog.generate_data import generate
# generate.run()

class BlogView(TemplateView):
    template_name = "blog/posts.html"

class PostView(TemplateView):
    template_name = "blog/post.html"
