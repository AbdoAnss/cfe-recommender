from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'coverage_type']
    search_fields = ['user__username', 'coverage_type']
    readonly_fields = ['user', 'coverage_type', 'updated_at']
    list_filter = ['coverage_type']

admin.site.register(UserProfile, UserProfileAdmin)