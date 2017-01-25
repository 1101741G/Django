from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says this is the home page! <br/>  <a href = '/rango/about/'> About</a>")

from django.http import HttpResponse
def about(request):
    return HttpResponse("Rango says this is the about page! <br/>  <a href = '/rango/'> Home</a>" )
