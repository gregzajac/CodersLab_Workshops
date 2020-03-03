from django.urls import path
from MyRent import views


urlpatterns = [
    path('', views.FlatListView.as_view(), name="flat-list"),
    path('agreement/', views.AgreementListView.as_view(), name="agreement-list"),
    #path('operation/', views.OperationListView.as_view(), name="operation-list"),
    #path('flat/<int:pk>', views.FlatDetailView.as_view(), name="flat-detail"),
    path('agreement/<int:pk>', views.AgreementDetailView.as_view(), name="agreement-detail"),

]
