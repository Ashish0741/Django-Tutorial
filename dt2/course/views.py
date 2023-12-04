from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django Tutorial')

def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('<h1> Hi Python </h1>')

def learn_var(request):
    addition = 10 + 30
    return HttpResponse(addition)

def learn_format(request):
    name = 'GeekyShows'
    return HttpResponse(f'Thanks {name} for in-depth django tutorial')
