from django.db import models

# Create your models here.
class students(models.Model):
    name1=models.CharField(max_length=50)
    college1=models.CharField(max_length=100)
    course1=models.CharField(max_length=30)
    def __str__(self):
        return self.name1

    