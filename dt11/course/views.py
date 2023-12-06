from django.shortcuts import render

# Create your views here.
def course(request):
    course_details = {
        'name' : 'Django',
        'duration' : 10,
        'total_seats' : 50
    }
    return render(request, 'course/course.html', course_details)