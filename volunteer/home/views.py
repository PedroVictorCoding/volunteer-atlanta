from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def homepage(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')
