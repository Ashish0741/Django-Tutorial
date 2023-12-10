from django.shortcuts import render

# Create your views here.
def learn_django(request):
    details = {
        'title' : 'Learn Django | AK',
        'name' : 'Django',
        'fees' : 2000
    }
    return render(request, 'course/course.html', details)