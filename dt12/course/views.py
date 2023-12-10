from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(request):
    return render(request, 'course/course_details.html', {'text' : 'django is awesome'})

def display_datetime(request):
    date = datetime.now()
    return render(request, 'course/datetime-filters.html', {'date' : date})

def display_floatformat(request):
    floating_numbers = {
        'num1' : 56.23456,
        'num2' : 56.00,
        'num3' : 56.3700
    }
    return render(request, 'course/floatformat-filters.html', floating_numbers)

def conditional_statements(request):
    course_details = {
        'name' : 'Django',
        'seats' : 20,
        'check' : False
    }
    return render(request, 'course/conditional-statements.html', course_details)

def control_statements(request):
    students = {
        'names' : ['Ashish','Shivani','Yash','Saloni'] 
    }

    mul_students = {
        'st1' : {
            'name' : 'Ashish',
            'age' : 23
        },

        'st2' : {
            'name' : 'Shivani',
            'age' : 24
        },

        'st3' : {
            'name' : 'Saloni',
            'age' : 25
        },

        'st4' : {
            'name' : 'Yash',
            'age' : 28
        }
    }

    stud = {
        "students" : students,
        'nested_students' : mul_students 
    }
    return render(request, 'course/control-statements.html', stud)