from django.urls import path
from django.conf.urls import url
from . import views

# Your all urls here

urlpatterns = [
    path('', views.index, name='index'),
    path('Conntact_Us', views.Contact, name='Conntact Us'),
    path('Address_Book', views.Address_Book, name='Address Book'),
    path('edit_address/<int:id>', views.edit_address, name='Edit Book'),
    path('delete_address/<int:id>', views.delete_address, name='Delete Book'),
]