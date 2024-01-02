from django.contrib import admin
from enroll.models import Student

# creating ModelAdmin class to display all fields of table in admin interface
# registering model using decorator

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stuemail','stupass')

# Register your models here.
# admin.site.register(Student,StudentAdmin)