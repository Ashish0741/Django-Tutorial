from django.shortcuts import render

# Create your views here.
def fees_django(request):
    details = {
        'title' : 'Django Fees',
        'name' : 'Django',
        'fees' : 3000
    }
    return render(request, 'fees/feesone.html', details)