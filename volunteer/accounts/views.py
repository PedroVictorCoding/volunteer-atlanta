from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accounts.models import UserProfile
from django.urls import reverse_lazy
from accounts.form import SignupForm, EditProfileForm

def profile(request):
    if request.user.is_authenticated:
        args = {'user': request.user}
        return render(request, 'accounts/profile.html', args)
    else:
        return HttpResponseRedirect('/accounts/login')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    args = {'form': form}
    return render(request, 'accounts/signup.html', args)


class ProfileUpdate(UpdateView):
    model = UserProfile
    fields = ['image']
    template_name = 'accounts/editprofileform.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile
