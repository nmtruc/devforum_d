from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Profile, Skill


def search_profiles(request):
    search_query = ''
    if request.GET.get('q'):
        search_query = request.GET.get('q')
    skills = Skill.objects.filter(name__iexact=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) |
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )
    return profiles, search_query


def paginate_profiles(request, profiles, results):
    page = request.GET.get('page')
    results = 3
    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)
    left_index = (int(page)-2)
    if left_index < 1:
        left_index = 1
    right_index = (int(page)+3)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1
    custom_range = range(left_index, right_index)

    return custom_range, profiles
