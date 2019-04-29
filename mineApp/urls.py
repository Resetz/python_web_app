from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('oasis/',views.oasis,name="oasis"),
    path('about/',views.about,name="about")
    
] 