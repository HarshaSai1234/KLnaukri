from django.urls import path
from . import views
urlpatterns=[
    path('employerhomepage/',views.employerhomepage,name='employerhomepage'),
]