from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    return HttpResponse('I am from Django Fees')

def fees_python(request):
    return HttpResponse('I am from Python Fees')
