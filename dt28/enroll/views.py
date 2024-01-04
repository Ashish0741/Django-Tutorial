from django.shortcuts import render
from enroll.forms import StudentRegistration

# Create your views here.

def showformdata(request):
    student_form = StudentRegistration()
    student_form.order_fields(field_order=['first_name','email'])
    return render(request, 'enroll/studentregistration.html', {'form' : student_form})