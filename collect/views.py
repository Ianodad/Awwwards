from urllib import request
from .models import Profile, Projects, Categories

from django.shortcuts import redirect, render
from .forms import ProfileForm, ProjectsForm

from django.db.models import Q
# Create your views here.


def home(request):
    word = "This is a house"
    current_user = request.user

    projects = Projects.get_all_projects()

    return render(request, 'pages/home.html', {"word": word, "projects": projects})


def submission(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('home')
    else:
        form = ProjectsForm()
    return render(request, 'pages/submit.html', {"form": form})


def profile(request):
    current_user = request.user
    profile = Profile.objects.get(username=current_user)
    projects = Projects.objects.filter(user=current_user)

    return render(request, 'pages/profile.html', {" current_user": current_user, "profile": profile, "projects": projects})


def add_profile(request):
    user = request.user
    # profile=Profile.objects.get(username=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.username = user
            upload.save()
            return redirect('profile')
    else:
        form = ProfileForm()

    return render(request, 'pages/add_profile.html', {"form": form})


def search(request):

    query = request.GET.get('q')
    print(query)
    if query:
        results = Projects.objects.filter(
            Q(title__icontains=query))
    else:
        results = Projects.objects.all()
    return render(request, 'pages/search.html', {'results': results})


def view_project(request, project_id):
    project = Projects.objects.get(id=project_id)

    return render(request, 'pages/view_project.html', {"project": project})
