from django.urls import path
from . import views

urlpatterns = [
    path('learndj/', views.learn_django),
    path('datetime/', views.display_datetime),
    path('floatformat/', views.display_floatformat),
    path('conditionalstatements/', views.conditional_statements),
    path('controlstatements/', views.control_statements),
]