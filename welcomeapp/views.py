from django.shortcuts import render
from django.http import HttpResponse
def welcomeapp(request):
    return HttpResponse("""<html><body bgcolor=cyan><h1><center>welcome to python</center></h1></body></html>""")
# Create your views here.
