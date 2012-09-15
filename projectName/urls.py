# -*- coding: utf-8 -*-
from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(('djobs.views'),
    # Examples:
    # url(r'^$', 'djobs.views.home', name='home'),
    # url(r'^djobs/', include('djobs.foo.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(('vote.views'),
    url(r'^vote/$', 'show'),
    url(r'^vote/(?P<id>\d+)/up$', 'up'),
    url(r'^vote/(?P<id>\d+)/down$', 'down'),
)

urlpatterns += patterns('',
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
)

urlpatterns += patterns('',
    (r'^accounts/$',  include('django_openid_auth.urls')),
    (r'^openid/', include('django_openid_auth.urls')),
)

urlpatterns += patterns((''),
    #静态文件
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/gs/djobs/static/'}
    ),
)