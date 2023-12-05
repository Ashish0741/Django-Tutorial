from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse('Hello Django')

def learn_python(request):
    return HttpResponse('<h1> Hi Python </h1>')

def learn_var(request):
    variable = '<h2> Hello How are you </h2>'
    return HttpResponse(variable)

def learn_math(request):
    addition = 10 + 34
    return HttpResponse(addition)

def learn_format(request):
    name = 'GeekyShows'
    return HttpResponse(f'Thank you {name} for url dispatcher videos')