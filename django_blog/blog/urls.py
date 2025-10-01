from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# blog/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    # Registration
    path('register/', views.register_view, name='register'),

    # Login / Logout (Django builtin)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
]
