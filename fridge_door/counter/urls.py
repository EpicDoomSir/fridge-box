from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='counter-home'),
    path('about/', views.about, name='counter-about'),
]