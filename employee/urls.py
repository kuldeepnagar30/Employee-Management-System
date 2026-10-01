from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add',views.add,name='add'),
    path('view',views.view, name='view'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete_employee, name='delete_employee'),
]