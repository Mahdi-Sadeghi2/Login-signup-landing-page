from . import views
from django.contrib.auth import views as auth
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('register/', views.register, name='register'),

]
