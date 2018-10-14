
from django.shortcuts import render


# Create your views here.


def home(request):
    word = "This is a house"

    return render(request, 'pages/home.html', {"word": word})
