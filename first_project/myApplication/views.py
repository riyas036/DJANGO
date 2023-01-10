from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    msg="<h1>Welcome to DJANGO</h1>"
    return HttpResponse(msg)
def index(request):
    msg="<h1>This is the Index Page</h1>"
    return HttpResponse(msg)


