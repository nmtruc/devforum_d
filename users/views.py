from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile


def login_user(request):
    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            print('Username not exists')

        user = authenticate(request, username=username, password=password)

        if User is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print('Username or password is incorrect')

    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    main_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description='')
    context = {'profile': profile, 'main_skills': main_skills,
               'other_skills': other_skills}
    return render(request, 'user-profile.html', context)
