from django.contrib import admin
from . import models

admin.site.site_header = 'Storefront admin'
admin.site.register(models.Collection)
admin.site.register(models.Product)


# Register your models here.
