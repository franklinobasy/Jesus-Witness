from django.urls import path

from .views import BlogView, PostView

app_name = "blog"

urlpatterns = [
    path("", BlogView.as_view(), name="blog_home"),
    path("post", PostView.as_view(), name='post')
]