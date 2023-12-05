from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    return HttpResponse('Hello DT8 Fees')

def fees_python(request):
    return HttpResponse('Hello PT8 Fees')
