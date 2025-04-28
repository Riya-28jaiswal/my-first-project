


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email=models.CharField(max_length=50,default='')
    message=models.CharField(max_length=200,default='')
    # Other fields and methods for your Contact model


