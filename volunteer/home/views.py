from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.forms import HomeForm
from home.models import Post

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-date')
        random_posts = Post.objects.order_by('?').first()
        users = User.objects.all()
        args = {'form': form, 'posts': posts, 'random_posts': random_posts, 'users': users}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            address = form.cleaned_data['address']
            website = form.cleaned_data['website']
            form = HomeForm()

        args = {'form': form}
        return render(request, self.template_name, args)


def about(request):
    return render(request, 'home/about.html')
