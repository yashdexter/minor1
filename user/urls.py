from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.userhome),
    path('userhome/',views.userhome),
    path('addpost/',views.addpost),
    path('viewpost/',views.viewpost),
    path('viewdeeppost/',views.viewdeeppost)


]
