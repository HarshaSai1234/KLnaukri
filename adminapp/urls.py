from django.urls import path
from . import views
urlpatterns=[
    path('',views.adminapphomepage,name='adminapphomepage'),
    path('printer/',views.printer,name='printer'),
    path('timetable/',views.timetable,name='timetable'),
    path('timezone1/',views.timezone1,name='timezone1'),
    path('signup/',views.signup,name='signup'),
    path('weather/',views.weather,name='weather'),
]