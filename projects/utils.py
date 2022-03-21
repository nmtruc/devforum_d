from django.db.models import Q
from .models import Project, Tag


def search_projects(request):
    search_query = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')
    tags = Tag.objects.filter(name__iexact=search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(owner__name__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query
