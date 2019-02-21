from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,'input.html')
def add(request):
    a=request.GET["t1"]
    b=request.GET["t2"]
    try:
        i=int(a)
        j=int(b)
        k=i+j
        return HttpResponse("<html><body bg color=gray><h1>sum is:"+str(k)+"</h1></body></html>")
    except(ValueError):
        return render(request,'input.html')

        # Create your views here.
