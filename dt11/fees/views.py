from django.shortcuts import render

# Create your views here.
def fees(request):
    fees_details = {
        'cname' : 'Django',
        'fees' : 3000
    }
    return render(request, 'fees/fees.html', fees_details)