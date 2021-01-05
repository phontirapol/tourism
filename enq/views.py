from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def instruction(request):
    return HttpResponse('This is English instruction')