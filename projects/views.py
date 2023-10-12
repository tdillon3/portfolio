from django.shortcuts import render

# Create your views here.
from .models import Project

def homepage(request):
    projects = Project.objects.all()
    return render(request, 'projects/home.html', {'projects': projects})
def resume(request):   # Add this function for the resume page
    projects = Project.objects.all()
    return render(request, 'projects/resume.html', {'projects': projects})