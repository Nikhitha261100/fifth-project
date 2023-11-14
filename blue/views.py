from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def keerthi(request):
    return render(request,'keerthi.html')

def sunny(request):
    return HttpResponse('<h1>this is sunny</h1>')