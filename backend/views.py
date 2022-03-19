from django.shortcuts import redirect, render
from .models import *
from .forms import *


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    context = {'project': project, 'tags': tags}
    return render(request, 'single-project.html', context)


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project-form.html', context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, 'project-form.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete-form.html', context)
