from django.test import TestCase

from .models import Program, Student


class StudentListTests(TestCase):
    def setUp(self):
        self.program = Program.objects.create(name='BSIT')
        for i in range(3):
            Student.objects.create(full_name=f'Student {i + 1}', program=self.program, year_level=i + 1)

    def test_student_list_page_renders(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student 1')

    def test_optimized_student_list_page_renders(self):
        response = self.client.get('/students/optimized/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Optimized Student List')
