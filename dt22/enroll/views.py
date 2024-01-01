from django.shortcuts import render
from enroll.models import Student

# Create your views here.
def studentinfo(request):
    students = Student.objects.all()
    return render(request, 'enroll/studentdetails.html',{'students' : students})
