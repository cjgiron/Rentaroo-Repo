from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('thanks/', views.thanks),
    path('create_listing', views.create_listing),
    path('all_apartments', views.all_apartments),
    path('login_process', views.login_process),
    path('register_process', views.register_process),	   
]