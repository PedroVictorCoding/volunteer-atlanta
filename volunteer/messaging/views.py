from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from django.views.generic import TemplateView
import json
from django.views.generic import TemplateView
from django.contrib.admin.models import ADDITION, LogEntry
from .models import Message
from .forms import MessageForm

@login_required
def home(request):
    return render(request, 'messaging/home.html')

@login_required
def room(request, room_name):
    return render(request, 'messaging/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    })

class RoomView(TemplateView):
    template_name = 'messaging/room.html'

    @method_decorator(login_required)
    def get(self, request, room_name):
        form        = MessageForm()
        messages    = Message.objects.order_by('timestamp').filter(room=room_name)
        args            = {'form': form, 'messages': messages}
        print(room_name)
        return render(request, self.template_name, args)
    def post(self, request, room_name):
        form = MessageForm(request.POST)
        if form.is_valid():
            message         = form.save(commit=False)
            message.room    = room_name
            message.author    = request.user
            content         = form.cleaned_data['message']
            message.save()
            form            = MessageForm()
            return HttpResponseRedirect('/room/'+ room_name)
        args        = {'form': form}
        print(room_name)
        return render(request, self.template_name, args)
