from django.contrib import admin
from .models import Student, Program  # Remove Program if you don't have a Program model

admin.site.register(Student)
admin.site.register(Program)