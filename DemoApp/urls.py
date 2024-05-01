

from django.urls import path
from DemoApp import views

urlpatterns = [
    path('', views.home, name='home')
]
