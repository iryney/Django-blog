from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blogapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', 'blogapp.views.login'),
    url(r'^logout/$', 'blogapp.views.logout'),
    url(r'^create/$', 'blogapp.views.create'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^delete/$', 'blogapp.views.delete'),
)
