from django.urls import path
from . import views

urlpatterns = [
    path("stuinfo/",views.studentinfo, name="studentinfo")
]
