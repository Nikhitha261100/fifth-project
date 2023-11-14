from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sweety(request):
    return render(request,'sweety.html')

def nannu(request):
    return HttpResponse('<h1> this is nannu</h1>')