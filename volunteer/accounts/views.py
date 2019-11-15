from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accounts.models import UserProfile
from django.urls import reverse_lazy
from accounts.form import SignupForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.models import Post, Friend
from accounts.models import VolunteeringLog
from accounts.form import LogForm
from django.views.generic import TemplateView
from django.contrib.admin.models import ADDITION, LogEntry
from home.forms import HomeForm


@method_decorator(login_required, name='get')
class LogView(TemplateView):
    template_name = 'accounts/profile.html'

    @method_decorator(login_required)
    def get(self, request, pk=None):
        form            = LogForm()
        logs            = VolunteeringLog.objects.filter(user=request.user.id).order_by('-date_activity')
        user = User.objects.get(id=request.user.id)
        token = user.pk
        token = str(token).zfill(6)
        args            = {'form': form, 'logs': logs, 'token': token}
        return render(request, self.template_name, args)

    @method_decorator(login_required)
    def post(self, request):
        form = LogForm(request.POST)
        if form.is_valid():
            log                 = form.save(commit=False)
            log.user            = request.user
            log.save()
            agency_name         = form.cleaned_data['agency_name']
            activity            = form.cleaned_data['activity']
            hours               = form.cleaned_data['hours']
            date_activity       = form.cleaned_data['date_activity']
            supervisor_contact  = form.cleaned_data['supervisor_contact']
            signature           = form.cleaned_data['signature']
            form                = LogForm()
            return HttpResponseRedirect('/accounts/profile')
        args = {'form': form}
        return render(request, self.template_name, args)


'''
@login_required
def profile(request,pk=None):
    user    = request.user
    users   = User.objects.exclude(id=request.user.id)
    args    = {'user': user, 'users': users}
    return render(request, 'accounts/profile.html', args)
'''

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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
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
