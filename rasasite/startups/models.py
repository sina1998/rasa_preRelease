# startups/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)

class Startup(models.Model):
    name = models.CharField(max_length=100)
    founder = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    skills_needed = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField(Skill)
    created_at = models.DateTimeField(auto_now_add=True)
