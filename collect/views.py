from urllib import request
from django.core.exceptions import ObjectDoesNotExist

from .models import Profile, Projects, Categories
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .forms import ProfileForm, ProjectsForm

from django.db.models import Q
# Create your views here.


def home(request):
    word = "This is a house"
    current_user = request.user

    projects = Projects.get_all_projects()

    return render(request, 'pages/home.html', {"word": word, "projects": projects})


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user

    try:
        profile = get_object_or_404(Profile, username=request.user)
    except ObjectDoesNotExist:
        return redirect('home')
        print("looking"+profile.profile_picture)

    return render(request, 'pages/profile.html', {" current_user": current_user, "profile": profile, "projects": projects})


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def search(request):

    query = request.GET.get('q')
    print(query)
    if query:
        results = Projects.objects.filter(
            Q(title__icontains=query))
    else:
        results = Projects.objects.all()
    return render(request, 'pages/search.html', {'results': results})


@login_required(login_url='/accounts/login/')
def view_project(request, project_id):
    project = Projects.objects.get(id=project_id)

    return render(request, 'pages/view_project.html', {"project": project})
