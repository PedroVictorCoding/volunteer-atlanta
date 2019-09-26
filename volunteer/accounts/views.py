from django.shortcuts import render, HttpResponse, HttpResponseRedirect

def profile(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    else:
        return HttpResponseRedirect('/accounts/login')

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'accounts/login.html')
