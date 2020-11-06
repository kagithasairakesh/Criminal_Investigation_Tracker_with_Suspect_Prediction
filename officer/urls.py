from django.urls import path
from officer import views

urlpatterns = [
    path('', views.home)
]