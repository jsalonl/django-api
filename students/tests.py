from django.test import TestCase
from students.models import Student
from django.utils import timezone

class StudentModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(name='Test Student', identification='1234567890')

    def test_student_creation(self):
        student = Student.objects.get(id=1)
        self.assertEqual(student.name, 'Test Student')
        self.assertEqual(student.identification, '1234567890')
        self.assertTrue(student.status)
        self.assertIsNotNone(student.created_at)
        self.assertIsNotNone(student.updated_at)

    def test_str_representation(self):
        student = Student.objects.get(id=1)
        self.assertEqual(str(student), 'Test Student')

    def test_model_defaults(self):
        # Test default values
        student = Student.objects.create(name='Another Student', identification='0987654321')
        self.assertTrue(student.status)  # Should be True by default
        self.assertEqual(student.created_at.date(), timezone.now().date())  # Auto_now_add should set the creation date
        self.assertEqual(student.updated_at.date(), timezone.now().date())  # Auto_now should set the update date to now
