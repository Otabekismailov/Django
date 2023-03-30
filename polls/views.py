from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hopage(request):
    return HttpResponse('<h1>hello word <h1>/')
