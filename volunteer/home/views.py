from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from home.forms import HomeForm

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm(auto_id=False)
        return render(request, self.template_name, {'form': form})


def homepage(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')
