from django.shortcuts import render

from .models import project


def index(request):
    projects = project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'index.html',context)
def details(request, pk):
    Projects= project.objects.get(pk=pk)
    context= {
        'projects':Projects
    }
    return render(request, 'details.html',context)
