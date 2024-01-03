from django.urls import path
from enroll import views

urlpatterns = [
    path('register/', views.showformdata, name='register'),
]
