from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # ex: /guru/
    url(r'^$', views.index, name='index'),
    # ex: /guru/1/
    url(r'^(?P<gas_station_id>\d+)/$', views.detail, name='detail'),
)

