from django.contrib import admin
from .models import Profile


# Register your models here.
# Set up the AdminModel for the Profile model
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "username", "email", "featured_image")


admin.site.register(Profile, ProfileAdmin)
