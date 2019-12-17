from django.shortcuts import render
from accounts.form import SignupForm

def lobby(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    args = {'form': form}
    return render(request, 'lobby/home2.html', args)
