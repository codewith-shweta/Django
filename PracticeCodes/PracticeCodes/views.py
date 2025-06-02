from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('Hello World')
    return render(request, 'website/index.html')

def dashboard(request):
    return HttpResponse("Welcome Here!")

def info(request):
    return HttpResponse('Log in..')  