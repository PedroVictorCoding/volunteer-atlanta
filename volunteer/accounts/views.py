from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accounts.models import UserProfile
from django.urls import reverse_lazy
from accounts.form import SignupForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.models import VolunteeringLog
from home.form import LogForm
from django.views.generic import TemplateView
from django.contrib.admin.models import ADDITION, LogEntry
from home.form import HomeForm
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from accounts.models import UserProfile


def profile(request):
    user = User.objects.get(id=request.user.id)
    user_profile = UserProfile.objects.get(user=request.user)
    user_profile = user_profile.clubs
    clubs_in = user_profile.split(",")
    token = user.pk
    token = str(token).zfill(6)
    args  = {'token': token, 'clubs_in': clubs_in}
    return render(request, 'accounts/profile.html')

@login_required
def other_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    form            = LogForm()
    token = user.pk
    token = str(token).zfill(6)
    logs            = VolunteeringLog.objects.filter(user=user)
    args            = {'form': form, 'logs': logs, 'user': user, 'token': token}
    return render(request, 'accounts/other_profile.html', args)

class Other_LogView(TemplateView):
    template_name = 'accounts/other_profile.html'
    def get(self, request):
        form            = LogForm()
        logs            = VolunteeringLog.objects.all().order_by('-')
        args            = {'form': form, 'logs': logs}
        return render(request, self.template_name, args)

def login(request):
    request = request.POST
    user = authenticate(request, username=request.cleaned_data['username'], password=request.cleaned_data['password'])
    if user is not None:
        login(request, user)
    else:
        return render(request, 'accounts/login_error.html')
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    args = {'form': form}
    return render(request, 'accounts/signup.html', args)


def view_post(request, pk=None):
    form            = LogForm()
    logs            = VolunteeringLog.objects.filter(pk=pk)
    args            = {'form': form, 'logs': logs}
    return render(request, 'accounts/view_post.html', args)


class ProfileUpdate(UpdateView):
    model           = UserProfile
    template_name   = 'accounts/editprofileform.html'
    success_url     = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile
