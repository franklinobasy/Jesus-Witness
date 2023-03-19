from typing import Dict, Any
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView, TemplateView

from blog.models import Post

from blog.generate_data import generate
# generate.run()

class BlogView(ListView):
    template_name = "blog/posts.html"
    model = Post
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data =  super().get_context_data(**kwargs)
        queryset = Post.objects.order_by('date_posted').all()
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            items = paginator.get_page(page)
        except PageNotAnInteger:
            items = paginator.page(1)
        except EmptyPage:
            items = paginator.page(paginator.num_pages)
        context_data['posts'] = items
        return context_data



class PostView(TemplateView):
    template_name = "blog/post.html"
