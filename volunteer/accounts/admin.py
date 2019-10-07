from django.contrib import admin
from accounts.models import UserProfile
from home.models import Post

class UserProfileAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        # Organizes the database by newest to oldest user
        queryset = queryset.order_by('-user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post)
