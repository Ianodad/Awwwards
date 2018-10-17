from urllib import request

from django.shortcuts import render
from .forms import ProfileForm, ProjectsForm

# Create your views here.


def home(request):
    word = "This is a house"
    current_user = request.user

    if request.method = 'POST'
        form = ProjectsForm(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('home')
        else:
            form = ProjectsForm()
    return render(request, 'pages/home.html', {"word": word})

def submission(request):

    if request.method ='POST'
        form = ProjectsForm(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('home')
    return render(request, 'pages/submit.html',{})

def profile(request):

    if request.method = 'POST'
        form = ProfileForm(request.POST)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
            return redirect('profile')
    return render(request, 'pages/profile.html'{})

    
