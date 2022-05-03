from django.urls import path
from . import views



app_name = 'cTracker' # to distinguish from other possible apps
urlpatterns = [
    path('', views.home, name='home'), # we have to write a view called home
    path("courses/", views.courses, name = 'courses'),
    path("courses/addcourse/", views.addcourse, name = 'addcourses'),
    path("courses/enroll/", views.enroll, name ='enroll'),
    path("homepage/", views.homepage, name = 'homepage'),


    ]