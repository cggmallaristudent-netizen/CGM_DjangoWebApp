from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/optimized/', views.student_list_optimized, name='student_list_optimized'),
]