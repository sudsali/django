from django.db import models

# Create your models here.

class Header(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    linkedin = models.URLField()
    github = models.URLField()

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    gpa = models.FloatField()
    start_year = models.IntegerField()
    finish_year = models.IntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class TechnicalSkill(models.Model):
    category = models.CharField(max_length=100) 
    skills = models.TextField()

    def __str__(self):
        return self.category
    
class Project(models.Model):
    name = models.CharField(max_length = 200)
    technologies_used = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null = True, blank = True)
    description = models.TextField()

    def __str__(self):
        return self.name

