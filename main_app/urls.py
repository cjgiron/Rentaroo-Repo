from django.urls import path     
from . import views
urlpatterns = [
    path('', views.get_city),
    path('thanks/', views.thanks),	   
]