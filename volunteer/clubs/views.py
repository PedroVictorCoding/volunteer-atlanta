from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
from accounts.models import UserProfile
from clubs.models import CheerItems
from clubs.form import CheerItemsForm

def home(request):
    user_profile = UserProfile.objects.get(user=request.user)
    clubs_in = user_profile.clubs
    indiv_clubs = clubs_in.split(',')
    indiv_clubs[:5]
    args = {'clubs_in': indiv_clubs}
    return render(request, 'clubs/home.html', args)

@login_required
def robotics(request):
    user_profile = UserProfile.objects.get(user=request.user)
    clubs_in = user_profile.clubs
    args = {'clubs_in': clubs_in}

    if request.is_ajax() and request.method == "POST":
      club = request.POST['ClubEntered']
      if user_profile.clubs == "":
          user_profile.clubs = club
      elif club in user_profile.clubs:
          pass
      else:
          user_profile.clubs = user_profile.clubs + "," + club
      user_profile.save()
      return HttpResponseRedirect(request, '/clubs/robotics/')
    else:
      return render(request, 'clubs/robotics/home.html', args)
    return render(request, 'clubs/robotics/home.html')

@login_required
def cheer_home(request, *args, **kwargs):
    user_profile = UserProfile.objects.get(user=request.user)
    clubs_in = user_profile.clubs
    args = {'clubs_in': clubs_in}

    if request.is_ajax() and request.method == "POST":
      club = request.POST['ClubEntered']
      if user_profile.clubs == "":
          user_profile.clubs = club
      elif club in user_profile.clubs:
          pass
      else:
          user_profile.clubs = user_profile.clubs + "," + club
      user_profile.save()
      return HttpResponseRedirect(request, '/clubs/cheerleading/')
    else:
      return render(request, 'clubs/cheer/home.html', args)
    return render(request, 'clubs/cheer/home.html', args)


class CheerItemsView(TemplateView):
    template_name = 'clubs/cheer/item_page.html'

    def get(self, request):
        form = CheerItemsForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CheerItemsForm(request.POST)
        if form.is_valid():
            cheer_items = form.save(commit=False)
            cheer_items.user = request.user
            cheer_items.save()
            items = form.cleaned_data['items']
            notes = form.cleaned_data['notes']
            form = CheerItemsForm()
            return HttpResponseRedirect('/clubs/cheerleading')
        args = {'form': form}
        return render(request, self.template_name, args)


class CheerView(TemplateView):
    template_name = 'clubs/cheer/.html'

    def get(self, request):
        if (request.GET.get('joinClub')):
            print("Joined Club")
        #form            = CheerForm()
        #args            = {'form': form, 'posts': posts, 'random_posts': random_posts, 'users': users}
        return render(request, self.template_name)


class CheerCoachView(TemplateView):
    template_name = "clubs/cheer/coach_home.html"
    args = {}
    def get(self, request):
        all_orders = CheerItems.objects.all()
        args = {'all_orders': all_orders}
        return render(request, self.template_name, args)
