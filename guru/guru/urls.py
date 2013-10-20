from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guru.views.home', name='home'),
    # url(r'^guru/', include('guru.foo.urls')),
    url(r'^guru/', include('fuel.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # user auth urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'guru.views.login', name='login'),
    url(r'^accounts/auth/$', 'guru.views.auth_view', name='auth_view'),
    url(r'^accounts/logout/$', 'guru.views.logout', name='logout'),
    url(r'^accounts/loggedin/$', 'guru.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'guru.views.invalid_login', name='invalid_login'),
    url(r'^accounts/register/$', 'guru.views.register_user', name='register_user'),
    url(r'^accounts/register_success/$', 'guru.views.register_success', name='register_success'),

)
