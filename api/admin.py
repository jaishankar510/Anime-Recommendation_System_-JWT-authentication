from django.contrib import admin

from .models import Anime, UserPreferences
# Register your models here.


admin.site.register(Anime)

admin.site.register(UserPreferences)
