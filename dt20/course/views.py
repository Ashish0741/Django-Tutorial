from django.shortcuts import render

# Create your views here.
def django_course(request):
    details = {
        'name' : 'Django',
        'fees' : 3000
    }
    return render(request, 'course/courseinfo.html', details)
