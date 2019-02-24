from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('incidencia/', views.incidence, name='incidence'),
    path('contacto/', views.contact, name='contact'),
    path('perfil/', views.profile, name='profile'),
    path('login', views.login, name='login')
]