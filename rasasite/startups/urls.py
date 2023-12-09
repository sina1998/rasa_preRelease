# startups/urls.py

from django.urls import path
from .views import register, create_startup, create_project, startup_detail, project_detail

urlpatterns = [
    path('register/', register, name='register'),
    path('create_startup/', create_startup, name='create_startup'),
    path('create_project/', create_project, name='create_project'),
    path('startup/<int:startup_id>/', startup_detail, name='startup_detail'),
    path('project/<int:project_id>/', project_detail, name='project_detail'),
]
