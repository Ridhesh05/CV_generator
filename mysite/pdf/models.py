from django.db import models

# Create your models here.
class Profile(models.Model):

    name =  models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=10,null=False)
    summary = models.TextField(max_length = 2000)
    degree = models.CharField(max_length = 100)
    school = models.CharField(max_length= 400)
    skills = models.CharField(max_length=800)
    university = models.TextField(max_length = 520)
    previous_work=models.TextField(max_length=2000)

    def __str__(self):
        return self.name
    