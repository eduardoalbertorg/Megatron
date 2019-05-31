from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import token_views
from . import views as main_views
from .router import router

app_name = 'main'


urlpatterns = [
    path('', main_views.homepage, name='homepage'),
    path('api/', include(router.urls)),
    path('api-token-auth/', token_views.obtain_auth_token, name='api-token-auth'),
    path('incidencia/', main_views.incidence, name='incidence'),
    path('registros/', main_views.attendance_record, name='attendance_records'),
    path('contacto/', main_views.contact, name='contact'),
    path('perfil/', main_views.profile, name='profile'),
    path('register/', main_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]