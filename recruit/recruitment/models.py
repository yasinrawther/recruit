from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    phone_number = models.CharField(max_length=30)
    address = models.TextField(null=True, blank=True)
    total_experience = models.FloatField()
    status = models.CharField(max_length=20, default='pending')


class EducationalDetails(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	education_name = models.CharField(max_length=200)
	marks_percentage = models.FloatField()
	institution_name = models.TextField()
	year_of_passed_out = models.DateField()


class SkillsDetails(models.Model):
	skill_name = models.CharField(max_length=200)
	years_of_experience = models.FloatField(max_length=10)


class ExperienceDetails(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	project_name = models.CharField(max_length=200)
	project_description = models.TextField()
	duration_from = models.DateField()
	duration_to = models.DateField()
	role_and_responsibility = models.TextField()




