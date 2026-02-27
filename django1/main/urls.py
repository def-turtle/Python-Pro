from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('resources/', views.resources, name='resources'),
    path('pricing/', views.pricing, name='pricing'),
    path('profile/', views.profile, name='profile'),
]