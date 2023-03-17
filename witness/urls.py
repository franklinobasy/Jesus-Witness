from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "witness"

urlpatterns = [
    path('register/', views.register, name='register'),

    path(
        'register/viewer/',
        views.register_viewer,
        name='register_viewer'
    ),

    path(
        'register/editor',
        views.register_editor,
        name='register_editor'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(template_name='witness/login.html'),
        name='login'
    ),
]
