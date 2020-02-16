"""workshop3bis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contactbox.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PersonList.as_view(), name='person_list'),
    path('person/<int:id>', PersonDetail.as_view(), name='person_detail'),
    path('delete/<int:id>', DeletePerson.as_view(), name='delete_person'),
    path('new-person/', NewPerson.as_view(), name='new_person'),
    path('new-address/', NewAddress.as_view(), name='new_address'),
    path('person/<int:id>/add-phone/', NewPhone.as_view(), name='new_phone'),
    path('person/<int:id>/add-email/', NewEmail.as_view(), name='new_email'),
    path('person/<int:id>/modify/', ModifyPerson.as_view(), name='modify_person'),
    path('person/<int:id>/delete-phone/<int:id_phone>', DeletePhone.as_view(), name='delete_phone'),
    path('person/<int:id>/delete-email/<int:id_email>', DeleteEmail.as_view(), name='delete_email'),
    path('groups/', GroupList.as_view(), name='group_list'),
    path('add-group/', NewGroup.as_view(), name='new_group'),
    path('group/<int:id>', GroupDetail.as_view(), name='group_detail'),
    path('delete-group/<int:id>', DeleteGroup.as_view(), name='delete-group'),
    path('group/<int:id>/add-person', NewPersonInGroup.as_view(), name='add_person_to_group'),
    path('group/<int:id>/delete-person/<int:id_person>', DeletePersonFromGroup.as_view(), name='delete_person_from_group'),
]
