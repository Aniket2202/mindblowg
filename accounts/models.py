from django.db import models

# Create your models here.
class intermediateVerficationModal(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    verificationStatus = models.BooleanField()
    otp = models.CharField(max_length=1000)
