# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import get_object_or_404, get_list_or_404, render

# Create your views here.
from .models import City, Neighborhood


def cities(request):
	cities = get_list_or_404(City)[:5]
	return render(request, 'city/index.html', {'cities':cities})


def city_show(request, city_id):
	city = get_object_or_404(City, pk=city_id)
	return render(request, 'city/show.html', {'city':city})


def neighborhoods(request):
	neighborhoods = get_list_or_404(Neighborhood)
	return render(request, 'neighborhood/index.html', {'neighborhoods': neighborhoods})


def neighborhood_show(request, neighborhood_id):
	neighborhood = get_object_or_404(Neighborhood, pk=neighborhood_id)
	return render(request, 'neighborhood/show.html', {'neighborhood':neighborhood})