from django.urls import path
from . import views

urlpatterns = [
    path('', views.instruction, name='en-instruction'),
]