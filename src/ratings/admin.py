from django.contrib import admin

# Register your models here.

from .models import Rating

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','content_object', 'value', 'active']
    raw_id_fields = ['user']
    readonly_fields = ['content_object']
    search_fields = ['user__username']
    list_filter = ['active']

    


admin.site.register(Rating, RatingAdmin)

