from django.db import models

# Create your models here.
class Employerdetails(models.Model):
    empid=models.CharField(max_length=120,primary_key=True)
    empname=models.CharField(max_length=120)
    emplocation=models.CharField(max_length=120)
    empphone=models.CharField(max_length=120)
    empemail=models.CharField(max_length=120)

    def __str__(self):
        return self.empname