from django.db import models

# Create your models here.
class hdfc(models.Model):
    fname = models.CharField(max_length = 25)
    lname = models.CharField(max_length= 25)

