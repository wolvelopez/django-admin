from django.conf.urls import patterns, include, url
#from django.contrib.auth import login, logout_then_login
from django.contrib import admin
from usuarios.views import inicio

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cseg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', inicio),
    #incluir la app de usuarios
    url(r'^usuarios/', include('usuarios.urls')),

)
