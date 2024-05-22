from django.shortcuts import render
from projects.models import Project
def home(request):
    if request.method == "GET":
        projects = Project.objects.all()
        context = {
            'projects': projects
        }    
        return render(request,'index.html', context=context)
    else:
        context = {
            'error': 'Error al mostrar el projecto',
        }
        return render(request,'index.html', context=context)
    