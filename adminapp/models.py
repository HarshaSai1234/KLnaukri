from django.db import models

# Create your models here.
class useraccount(models.Model):
    ROLE_CHOICES = [
        ('employer', 'Employer'),
        ('jobseeker', 'Jobseeker'),
    ]
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    email = models.EmailField(primary_key=True)
    pnumber = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    password = models.CharField(max_length=120)
    def __str__(self):
        return self.fname

class StudentFeedback(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.EmailField()
    course_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comments = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.student_name