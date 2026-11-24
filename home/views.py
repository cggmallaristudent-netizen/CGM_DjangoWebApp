from django.shortcuts import render

from .models import Student


def index(request):
    student_count = Student.objects.count()
    return render(request, 'home/index.html', {'student_count': student_count})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'home/student_list.html', {'students': students})


def student_list_optimized(request):
    students = Student.objects.select_related('program').all()
    return render(request, 'home/student_list_optimized.html', {'students': students})