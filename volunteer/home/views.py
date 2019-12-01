from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accounts.models import UserProfile
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from home.models import Post
from home.models import VolunteeringLog, VolunteeringQuestions
from home.form import LogForm, HomeForm, VolunteerQuestionsForm
from django.views.generic import TemplateView
from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form            = HomeForm()
        posts           = Post.objects.all().order_by('-date')
        random_posts    = Post.objects.order_by('?').first()
        #users           = User.objects.exclude(id=request.user.id)
        users           = User.objects.order_by('?').exclude(id=request.user.id)[:4]
        args            = {'form': form, 'posts': posts, 'random_posts': random_posts, 'users': users}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post            = form.save(commit=False)
            post.user       = request.user
            post.save()
            title           = form.cleaned_data['title']
            description     = form.cleaned_data['description']
            address         = form.cleaned_data['address']
            website         = form.cleaned_data['website']
            category_tag    = form.cleaned_data['category_tag']
            form            = HomeForm()
            return HttpResponseRedirect('/volunteer')

        args = {'form': form}
        return render(request, self.template_name, args)


def about(request):
    return render(request, 'home/about.html')


def creators(request):
    return render(request, 'home/creators.html')


class LogView(TemplateView):
    template_name = 'home/volunteer.html'

    @method_decorator(login_required)
    def get(self, request, pk=None):
        form            = LogForm()
        questions       = VolunteerQuestionsForm()
        logs            = VolunteeringLog.objects.filter(user=request.user.id).order_by('-date_activity')
        question_val    = VolunteeringQuestions.objects.filter(user=request.user.id)
        args  = {'form': form, 'logs': logs, 'questions': questions, 'question_val': question_val}
        return render(request, self.template_name, args)

    @method_decorator(login_required)
    def post(self, request):
        form = LogForm(request.POST)
        questions = VolunteerQuestionsForm(request.POST)
        if form.is_valid():
            log                 = form.save(commit=False)
            log.user            = request.user
            agency_name         = form.cleaned_data['agency_name']
            activity            = form.cleaned_data['activity']
            hours               = form.cleaned_data['hours']
            date_activity       = form.cleaned_data['date_activity']
            supervisor_contact  = form.cleaned_data['supervisor_contact']
            signature           = form.cleaned_data['signature']
            log.save()
            form                = LogForm()
            return HttpResponseRedirect('/volunteer/log')


        question_val    = VolunteeringQuestions.objects.filter(user=request.user.id)
        if not question_val:
            if questions.is_valid():
                question            = questions.save(commit=False)
                question.user       = request.user
                question1           = questions.cleaned_data['question1']
                question2           = questions.cleaned_data['question2']
                question3           = questions.cleaned_data['question3']
                question4           = questions.cleaned_data['question4']
                question.save()
                return HttpResponseRedirect('/volunteer/log')
        elif question_val:
            if questions.is_valid():
                question = VolunteeringQuestions.objects.filter(user=request.user.id)
                question.update(question1=questions.cleaned_data['question1'])
                question.update(question2=questions.cleaned_data['question2'])
                question.update(question3=questions.cleaned_data['question3'])
                question.update(question4=questions.cleaned_data['question4'])
                questions = VolunteerQuestionsForm()
        args = {'form': form, 'questions': questions}
        return render(request, self.template_name, args)
