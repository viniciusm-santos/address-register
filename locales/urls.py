from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^neighborhood/$', views.neighborhoods, name='neighborhood_index'),
	url(r'^neighborhood/(?P<neighborhood_id>[0-9]+)/$', views.neighborhood_show, name='neighborhood_show'),
    url(r'^city/$', views.cities, name='city_index'),
    url(r'^city/(?P<city_id>[0-9]+)/$', views.city_show, name='city_show'),
]