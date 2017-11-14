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
from mxvscorrupcion.views import Kondo_Admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.loginUser, name='index'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^admin/', admin.site.urls, name='django-admin'),
    url(r'^empresa/', views.empresa, name='empresa'),
    url(r'^login/', views.loginUser, name='login'),
    # url(r'^edit/', views.editInfo, name='edit-info'),
    url(r'^signin/', views.register, name='register'),
    url(r'^articulos/(?P<slug>[-\w]+)/$', views.articulos, name='articulos'),
    url(r'^modify-answer/(?P<pk>[0-9 a-z]+)/$', views.modifyAnswer, name='modify-answer'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^revisor/', views.revisor, name='revisor'),
    url(r'^validate/(?P<pk>[0-9]+)/(?P<empresa_pk>[0-9]+)/', views.validate, name='validate'),
    # url(r'^empresas/', views.import_empresas, name='validate'),
    # url(r'^empresas_final/', views.import_empresas_final, name='empresas_final'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^send-mail/', views.send_email, name='send_email'),
    url(r'^admin-users/', views.usersAdmin, name='admin-users'),
    url(r'recientes/', views.entradasRecientes, name='entradas-recientes'),
    url(r'articulos/', views.blog_articulos, name='blog_articulos'),
    url(r'articulo/(?P<slug>[-\w]+)/$', views.getArticleSlug, name='article-slug'),

    # kondo-admin
    url(r'^kondo-admin/corte/(?P<pk>[0-9]+)/$', views.Corte_Detail.as_view(), name='corte'),
    url(r'^kondo-admin/$', Kondo_Admin.as_view(), name='kondo_admin'),
    url(r'^reject-question/$', views.rejectQuestion, name='pregunta-rechazada'),

    #CRUD GLOSARIO
    url(r'^glosario/create/$', views.CreateGlosario.as_view(), name='create_glosario'),
    url(r'^glosario/update/(?P<pk>[0-9 a-z]+)/$', views.UpdateGlosario.as_view(), name='update_glosario'),
    url(r'^glosario/delete/(?P<pk>[0-9 a-z]+)/$', views.DeleteGlosario.as_view(), name='delete_glosario'),
    url(r'^glosario/list/$', views.ListGlosario.as_view(), name='list_glosario'),
    url(r'^glosario/', views.glosario, name='glosario'),

    #CRUD FUENTES
    url(r'^fuentes/create/$', views.CreateFuente.as_view(), name='create_fuente'),
    url(r'^fuentes/update/(?P<pk>[0-9 a-z]+)/$', views.UpdateFuente.as_view(), name='update_fuente'),
    url(r'^fuentes/delete/(?P<pk>[0-9 a-z]+)/$', views.DeleteFuente.as_view(), name='delete_fuente'),
    url(r'^fuentes/list/$', views.ListFuente.as_view(), name='list_fuente'),
    url(r'^fuentes/', views.fuentes, name='fuentes'),

    #CRUD PAISES
    url(r'^paises/create/$', views.CreatePaises.as_view(), name='create_paises'),
    url(r'^paises/update/(?P<pk>[0-9 a-z]+)/$', views.UpdatePaises.as_view(), name='update_paises'),
    url(r'^paises/delete/(?P<pk>[0-9 a-z]+)/$', views.DeletePaises.as_view(), name='delete_paises'),
    url(r'^paises/$', views.ListPaises.as_view(), name='list_paises'),

    #CRUD CUESTIONARIO
    url(r'^cuestionario/create/$', views.CreateCuestionario.as_view(), name='create_cuestionario'),
    url(r'^cuestionario/update/(?P<pk>[0-9 a-z]+)/$', views.UpdateCuestionario.as_view(), name='update_cuestionario'),
    url(r'^cuestionario/delete/(?P<pk>[0-9 a-z]+)/$', views.DeleteCuestionario.as_view(), name='delete_cuestionario'),
    url(r'^cuestionario/list/$', views.ListCuestionario.as_view(), name='list_cuestionario'),

    #CRUD RESPUESTAS
    url(r'^respuestas/create/$', views.CreateRespuesta.as_view(), name='create_respuestas'),
    url(r'^respuestas/update/(?P<pk>[0-9 a-z]+)/$', views.UpdateRespuesta.as_view(), name='update_respuestas'),
    url(r'^respuestas/delete/(?P<pk>[0-9 a-z]+)/$', views.DeleteRespuesta.as_view(), name='delete_respuestas'),
    url(r'^respuestas/list/$', views.ListRespuesta.as_view(), name='list_respuestas'),
  
    url(r'^new-corte/', views.new_corte, name='new-corte'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
