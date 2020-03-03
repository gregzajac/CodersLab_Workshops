from django.shortcuts import render
from django.views.generic import ListView, DetailView
from MyRent.models import Flat, Agreement, Operation, Tenant


class FlatListView(ListView):
    model = Flat

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            flats = Flat.objects.all().order_by("-is_for_rent")
        else:
            flats = Flat.objects.filter(is_for_rent=True)
        return flats

# class FlatDetailView(DetailView):
#     model = Flat


class AgreementListView(ListView):
    model = Agreement

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            agreements = Agreement.objects.all().order_by("-agreement_date")
        else:
            tenant = Tenant.objects.get(user=user)
            agreements = Agreement.objects.filter(tenant=tenant).order_by("-agreement_date")
        return agreements


class AgreementDetailView(DetailView):
    model = Agreement

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=None, **kwargs)
        operations = Operation.objects.filter(agreement=self.object).order_by("date")
        ctx.update({'operations': operations})

        balance = 0
        for operation in operations:
            if operation.type.plus_minus == 2:  #zobowiązania
                balance -= operation.value
            elif operation.type.plus_minus == 1:  #należności
                balance += operation.value
        ctx.update({'balance': balance})
        return ctx


# class OperationListView(ListView):
#     model = Operation
#
#     def get_queryset(self):
#         user = self.request.user
#         tenant = Tenant.objects.get(user=user)
#         agreements = Agreement.objects.filter(tenant=tenant)
#         operations = Operation.objects.filter(agreement__in=agreements)
#         return operations
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         ctx = super().get_context_data(object_list=None, **kwargs)
#         user = self.request.user
#         tenant = Tenant.objects.get(user=user)
#         agreements = Agreement.objects.filter(tenant=tenant)
#         ctx.update({'agreements': agreements})
#         return ctx
