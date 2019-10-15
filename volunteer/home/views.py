from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.forms import HomeForm
from home.models import Post, Friend

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
            return HttpResponseRedirect('home:home')

        args = {'form': form}
        return render(request, self.template_name, args)


def about(request):
    return render(request, 'home/about.html')

def change_friend(request, operation, pk):
    new_friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, new_friend)
    elif operation == 'remove':
        Friend.remove_friend(request.user, new_friend)
    return HttpResponseRedirect('/')
