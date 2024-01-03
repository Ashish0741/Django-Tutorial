from django.shortcuts import render
from enroll.forms import StudentRegistration

# Create your views here.

def showformdata(request):
    student_form = StudentRegistration(auto_id=True, label_suffix=' -> ', initial={'name' : 'Ashish'})
    return render(request, 'enroll/studentregistration.html', {'form' : student_form})