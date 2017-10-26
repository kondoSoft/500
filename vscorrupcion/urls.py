"""vscorrupcion4 URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import logout
from mxvscorrupcion import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^empresa/', views.empresa, name='empresa'),
    url(r'^login/', views.loginUser, name='login'),
    url(r'^edit/', views.editInfo, name='edit-info'),
    url(r'^signin/', views.register, name='register'),
    url(r'^articulos/(?P<slug>[-\w]+)/$', views.articulos, name='articulos'),
    url(r'^modify-answer/(?P<pk>[0-9 a-z]+)/$', views.modifyAnswer, name='modify-answer'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^revisor/', views.revisor, name='revisor'),
    url(r'^validate/', views.validate, name='validate'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^glosario/', views.glosario, name='glosario'),
    url(r'^fuentes/', views.fuentes, name='fuentes')
]
