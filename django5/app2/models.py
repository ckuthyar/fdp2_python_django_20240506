from django.db import models

class icici(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    aadhar=models.IntegerField(max_length=12)
    pincode=models.IntegerField(max_length=6)

    def __str__(self):
        return self.lname