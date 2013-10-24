from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    # ex: /guru/
    url(regex=r'^$',
        view=views.index,
        name='index'),

    # ex: /guru/1/
    url(regex=r'^(?P<gas_station_id>\d+)/$',
        view=views.detail,
        name='detail'),
)

