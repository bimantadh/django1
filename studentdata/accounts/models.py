from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.CharField(
                max_length=50,
                null=False,
                unique=True
                )
    faculty = models.CharField(max_length=40)
    grade = models.IntegerField()
    mobile = models.CharField()

    

    
    