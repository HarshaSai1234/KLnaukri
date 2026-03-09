from django.db import models

# Create your models here.
class jobseekerprofile(models.Model):
    name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    hobbies=models.TextField()
    skills=models.TextField()
    address=models.TextField()
    profile_photo=models.ImageField(upload_to='profile_pics/')

    def __str__(self):
        return self.name

