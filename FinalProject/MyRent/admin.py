from django.contrib import admin

from MyRent.models import Flat, Tenant, Agreement, Operation, OperationDict, Landlord

admin.site.register(Flat)
admin.site.register(Tenant)
admin.site.register(Agreement)
admin.site.register(Operation)
admin.site.register(OperationDict)
admin.site.register(Landlord)
