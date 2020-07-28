from django.urls import path
from counter import views

app_name = 'counter'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('homepage/', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
]