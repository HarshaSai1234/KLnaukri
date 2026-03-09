from django.urls import path
from . import views
urlpatterns=[
    path('jobseekerhomepage/',views.jobseekerhomepage,name='jobseekerhomepage'),
    path('profilelist/',views.profilelist,name='profilelist'),
    path('addprofile/',views.addprofile,name='addprofile'),
]