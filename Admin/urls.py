from django.urls import path
from Admin import views


urlpatterns = [
    path('', views.home),
    path('create', views.create),
    path('retrieve', views.retrieve),
]