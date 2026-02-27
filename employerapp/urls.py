from django.urls import path
from . import views
urlpatterns=[
    path('employerhomepage/',views.employerhomepage,name='employerhomepage'),
    path('crudfunction/',views.crudfunction,name='crudfunction'),
    path('crud_insert/',views.crud_insert,name='crud_insert'),
    path('read_employee/',views.read_employee,name='read_employee'),
    path('update_employee/',views.update_employee,name='update_employee'),
    path('delete_employee/',views.delete_employee,name='delete_employee'),
]