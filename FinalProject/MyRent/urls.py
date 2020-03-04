from django.urls import path
from MyRent import views


urlpatterns = [
    path('', views.FlatListView.as_view(), name="flat-list"),
    path('add_flat', views.CreateFlatView.as_view(), name="add-flat"),
    path('agreement/', views.AgreementListView.as_view(), name="agreement-list"),
    #path('operation/', views.OperationListView.as_view(), name="operation-list"),
    path('flat/<int:pk>', views.FlatDetailView.as_view(), name="flat-detail"),
    path('flat/delete/<int:pk>', views.FlatDeleteView.as_view(), name="delete-flat"),
    path('flat/modify/<int:pk>', views.FlatUpdateView.as_view(), name="modify-flat"),
    path('agreement/<int:pk>', views.AgreementDetailView.as_view(), name="agreement-detail"),
    path('add_obligations/<int:id_agreement>', views.AddObligationsView.as_view(), name="add-obligations"),

]
