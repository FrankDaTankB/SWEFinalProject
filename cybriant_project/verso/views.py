from django.shortcuts import render


def home(request):
    return render(request, 'verso/login.html')


def index(request):
    return render(request, 'verso/index.html', {'title': 'Welcome'})
# Create your views here.
