from django.urls import path
from . import views
urlpatterns=[
    path('jobseekerhomepage/',views.jobseekerhomepage,name='jobseekerhomepage'),
]