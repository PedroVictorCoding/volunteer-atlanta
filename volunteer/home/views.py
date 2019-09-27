from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from home.forms import HomeForm
from home.models import Post

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-date')
        print(posts)
        args = {'form': form, 'posts': posts}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            website = form.cleaned_data['website']
            form = HomeForm()

        args = {'form': form}
        return render(request, self.template_name, args)


def homepage(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')
