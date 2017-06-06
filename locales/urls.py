from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^neighborhoods/$', views.neighborhoods, name='neighborhoods'),
	url(r'^neighborhoods/(?P<neighborhood_id>[0-9]+)/$', views.neighborhood_show, name='neighborhood_show'),
    url(r'^cities/$', views.cities, name='cities'),
    url(r'^cities/(?P<city_id>[0-9]+)/$', views.city_show, name='city_show'),
]