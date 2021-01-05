from django.urls import path
from . import views

urlpatterns = [
    path('', views.instruction, name='th-instruction'),
    path('question/', views.question, name='th-question'),
]