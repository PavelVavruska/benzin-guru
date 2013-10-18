from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guru.views.home', name='home'),
    # url(r'^guru/', include('guru.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'guru.views.login'),
    url(r'^accounts/auth/$', 'guru.views.auth_view'),
    url(r'^accounts/logout/$', 'guru.views.logout'),
    url(r'^accounts/loggedin/$', 'guru.views.loggedin'),
    url(r'^accounts/invalid/$', 'guru.views.invalid_login'),

)
