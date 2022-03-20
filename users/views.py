from django.shortcuts import redirect, render
from .models import *


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    main_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')
    context = {'profile': profile, 'main_skills': main_skills, 'other_skills': other_skills}
    return render(request, 'user-profile.html', context)
