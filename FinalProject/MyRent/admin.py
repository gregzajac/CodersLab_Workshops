from django.contrib import admin

from MyRent.models import Flat, Tenant, Agreement

admin.site.register(Flat)
admin.site.register(Tenant)
admin.site.register(Agreement)
