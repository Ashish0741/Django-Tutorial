from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    return HttpResponse(f'Django Fees: {500}')

def fees_python(request):
    return HttpResponse(f'Python Fees: {700}')
