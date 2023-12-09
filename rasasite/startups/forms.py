# startups/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile, Startup, Project

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio']

class StartupForm(forms.ModelForm):
    class Meta:
        model = Startup
        fields = ['name', 'description', 'skills_needed']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'skills_required']
