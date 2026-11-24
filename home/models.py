from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=100)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='students')
    year_level = models.PositiveIntegerField()

    def __str__(self):
        return self.full_name
