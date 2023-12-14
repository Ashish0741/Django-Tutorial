from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.django_course, name='djangocourse'),
]
