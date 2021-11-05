import inspect

from django.contrib import admin

from web import models

for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        admin.site.register(obj)