from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api', views.api, name='api'),
    path('mongo', views.mongo, name='mongo'),
]