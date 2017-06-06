# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class City(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Neighborhood(models.Model):
	name = models.CharField(max_length=100)
	city = models.ForeignKey(City, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
		return self.street