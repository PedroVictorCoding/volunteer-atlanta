from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
import json
from accounts.models import UserProfile

def home(request):
    return render(request, 'clubs/home.html')

def robotics(request):
    return render(request, 'clubs/robotics/home.html')
    

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
      return HttpResponse(json.dumps({'clubs_in': clubs_in}), content_type="application/json")
    else:
      return render(request, 'clubs/cheer/home.html', args)
    return render(request, 'clubs/cheer/home.html', args)


class CheerView(TemplateView):
    template_name = 'clubs/cheer/.html'

    def get(self, request):
        if (request.GET.get('joinClub')):
            print("Joined Club")
        #form            = CheerForm()
        #args            = {'form': form, 'posts': posts, 'random_posts': random_posts, 'users': users}
        return render(request, self.template_name)
