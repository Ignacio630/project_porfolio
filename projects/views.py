from django.shortcuts import render
from .models import Project
# Create your views here.

def projects_list(request):
    if request.method == "GET":
        projects = Project.objects.all()
        context = {
            'projects': projects
        }    
        return render(request, 'partials/projects_list.html', context=context)
    else:
        context = {
            'error': 'Error al mostrar el projecto',
        }
        return render(request, 'partials/projects_list.html', context=context)