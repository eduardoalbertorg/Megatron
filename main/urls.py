from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('incidencia/', views.incidence, name='incidence'),
    path('contacto/', views.contact, name='contact'),
    path('perfil/', views.profile, name='profile'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
]