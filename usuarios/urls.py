from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout_then_login
from usuarios.views import Registro, salir

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html'}, name='login'),
    url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),	
    url(r'^registro/$', Registro, name='registro'),
    url(r'^salir/$', salir, name='salir'),
)
