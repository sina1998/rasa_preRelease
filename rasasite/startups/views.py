# startups/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, Startup, Project, Skill
from .forms import UserProfileForm, StartupForm, ProjectForm

def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('dashboard')  # Redirect to user dashboard or home
    else:
        form = UserProfileForm()
    return render(request, 'startups/register.html', {'form': form})

@login_required
def create_startup(request):
    if request.method == 'POST':
        form = StartupForm(request.POST)
        if form.is_valid():
            startup = form.save(commit=False)
            startup.founder = request.user.userprofile
            startup.save()
            messages.success(request, 'Startup created successfully!')
            return redirect('dashboard')  # Redirect to user dashboard or home
    else:
        form = StartupForm()
    return render(request, 'startups/create_startup.html', {'form': form})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.startup = get_object_or_404(Startup, founder=request.user.userprofile)
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('dashboard')  # Redirect to user dashboard or home
    else:
        form = ProjectForm()
    return render(request, 'startups/create_project.html', {'form': form})

def startup_detail(request, startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)
    projects = Project.objects.filter(startup=startup)
    return render(request, 'startups/startup_detail.html', {'startup': startup, 'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'startups/project_detail.html', {'project': project})
