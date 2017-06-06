# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Address, City, Neighborhood

admin.site.register(Address)
admin.site.register(City)
admin.site.register(Neighborhood)