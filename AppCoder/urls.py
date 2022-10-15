from re import template
from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', inicio),
    path('cursos/',cursos),
    path('entregables/', entregables),
    path('estudiantes/',estudiantes),
    path('profesores/', profesores),
    path('home/',home),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiante/', buscar_estudiante),
    path('create_estudiantes/', create_estudiantes),
    path('read_estudiantes/', read_estudiantes),
    path('update_estudiantes/<estudiante_id>', update_estudiantes),
    path('delete_estudiantes/<estudiante_id>', delete_estudiantes),
    path('login/', login_request),
    path('registro/', registro),
    path('logout/', LogoutView.as_view(template_name = 'inicio.html'), name = "Logout"),
    path('perfil/editarPerfil/', editarPerfil),
    path('perfil/cambiarPassword/', cambiarPassword),
    path('perfil/', perfilView),
    path('perfil/changeAvatar', AgregarAvatar),
]

