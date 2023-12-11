from django.shortcuts import render

# Create your views here.
def learn_django(request):
    details = {
        'title' : 'Learn Django',
        'name' : 'Django'
    }
    return render(request, 'course/courseone.html', details)