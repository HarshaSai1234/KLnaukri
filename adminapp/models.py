from django.db import models

# Create your models here.
class useraccount(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Jobseeker'),
    ]
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    pnumber = models.IntegerField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    def __str__(self):
        return self.fname