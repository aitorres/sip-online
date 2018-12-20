"""sip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from gestion.views import cambiar_contrasena

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'sesiones/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^cambiar-contrasena/', cambiar_contrasena, name='cambiar-contrasena'),
    url(
        r'^resetear-contrasena/$',
        auth_views.password_reset,
        {
            'template_name': 'sesiones/reiniciar_contrasena.html'
        },
        name='password_reset'
    ),
    url(r'^resetear-contrasena/listo/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^resetear/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^resetear/listo/$', auth_views.password_reset_complete, name='resetear-contrasena'),
    url(r'^admin/', admin.site.urls),
    url(r'', include('gestion.urls')),
]
