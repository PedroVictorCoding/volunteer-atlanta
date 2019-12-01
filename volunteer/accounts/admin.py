from django.contrib import admin
from accounts.models import UserProfile
from home.models import Post
from home.models import VolunteeringLog, VolunteeringQuestions
from clubs.models import CheerItems

class UserProfileAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        # Organizes the database by newest to oldest user
        queryset = queryset.order_by('-user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post)
admin.site.register(VolunteeringLog)
admin.site.register(VolunteeringQuestions)

admin.site.register(CheerItems)
