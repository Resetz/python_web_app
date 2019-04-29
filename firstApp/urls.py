from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('coolwebsites/',views.coolwebsites,name="coolwebsites"),
    path('form/',views.form,name="form"),
    path('greet/',views.greet,name="greet"),
     path('register/',views.register,name="register")
] 