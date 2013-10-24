from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^guru/', include('fuel.urls')),  # fuel app urls
    url(r'^admin/', include(admin.site.urls)),  # admin urls
    # user auth urls
    url(regex=r'^accounts/login/$',
        view='guru.views.login',
        name='login'),
    url(regex=r'^accounts/auth/$',
        view='guru.views.auth_view',
        name='auth_view'),
    url(regex=r'^accounts/logout/$',
        view='guru.views.logout',
        name='logout'),
    url(regex=r'^accounts/loggedin/$',
        view='guru.views.loggedin',
        name='loggedin'),
    url(regex=r'^accounts/invalid/$',
        view='guru.views.invalid_login',
        name='invalid_login'),
    url(regex=r'^accounts/register/$',
        view='guru.views.register_user',
        name='register_user'),
    url(regex=r'^accounts/register_success/$',
        view='guru.views.register_success',
        name='register_success'),
)