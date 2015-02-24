from django.conf.urls import patterns, include, url
from django.contrib import admin
from sistema.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^cadastro_pessoa/$', 'sistema.views.cadastro_pessoa', name='cadastro_pessoa'),
	url(r'^editar_pessoa/(?P<id_pessoa>[0-9]+)/$', 'sistema.views.editar_pessoa', name='editar_pessoa'),	
	url(r'^excluir_pessoa/(?P<id_pessoa>[0-9]+)/$', 'sistema.views.excluir_pessoa', name='excluir_pessoa'),
	url(r'^visualizar_pessoas/$', 'sistema.views.visualizar_pessoas', name='visualizar_pessoas'),
	url(r'^login/$', 'sistema.views.login', name='login'),
    url(r'^logout/$', 'sistema.views.logout', name='logout'),
	url(r'^home/$', 'sistema.views.home', name='home'),
)
