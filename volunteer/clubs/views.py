from django.shortcuts import render

def home(request):
    return render(request, 'clubs/home.html')

def robotics(request):
    return render(request, 'clubs/robotics/home.html')
