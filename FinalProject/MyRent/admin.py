from django.contrib import admin
from MyRent.models import Flat, Tenant, Agreement, Operation, OperationDict, Landlord


class FlatAdmin(admin.ModelAdmin):
    model = Flat
    list_display = ('__str__', 'is_for_rent', 'info')


class TenantAdmin(admin.ModelAdmin):
    model = Tenant
    list_display = ('__str__', 'phone', 'email', 'info')


class AgreementAdmin(admin.ModelAdmin):
    model = Agreement
    list_display = ('code', 'agreement_date', 'date_from', 'date_to',
                    'mth_payment_value', 'mth_payment_deadline', 'info')


class OperationAdmin(admin.ModelAdmin):
    model = Operation
    list_display = ('__str__', 'info')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Operation, OperationAdmin)

admin.site.register(OperationDict)
admin.site.register(Landlord)
