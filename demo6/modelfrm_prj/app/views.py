from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
# Create your views here.



def fertility(request):
    return render(request, "crop.html")

def showdata(request):
    #return render(request, 'hello.html')
    data = Fertilizer.objects.all()
    return render(request, 'crop.html',{'data':data})
