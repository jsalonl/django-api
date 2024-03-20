from django.db import models

# Create your models here.
class Student(models.Model):
  name = models.CharField(max_length=200)
  identification = models.CharField(max_length=30)
  status = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  # This is the string representation of the model
  def __str__(self):
    return self.name