from django.urls import path
from . import views

urlpatterns = [
    path('fees-details/', views.fees),
]