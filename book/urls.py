"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from addresses.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("addresses/add/", AddPersonView.as_view(), name="add_person"),
    path("addresses/all/", GetAllPersonsView.as_view(), name="all"),
    path("addresses/contact_info/<int:id>/", ContactInfoView.as_view(), name="contact_info"),
    path("addresses/edit_cocntact/<int:pk>/", ContactEditView.as_view(), name="edit_contact"),
    path("addresses/del_cocntact/<int:pk>/", ContactDeleteView.as_view(), name="delete_contact"),
    path("addresses/add_group/", CreateGroupView.as_view(), name="add_group"),
    path("addresses/all_groups/", GroupListView.as_view(), name="all_groups"),
    path("addresses/group_info/<int:id>", GroupInfoView.as_view(), name="group_info"),
    path("addresses/edit_group/<int:pk>/", EditGroupView.as_view(), name="edit_group"),
    path("addresses/del_group/<int:pk>/", GroupDeleteView.as_view(), name="delete_group"),
]
