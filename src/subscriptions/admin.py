from django.contrib import admin

# Register your models here.
from .models import Subscription

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','__str__', 'rating_last_updated', 'rating_count', 'rating_avg']
    readonly_fields = ['rating_count', 'rating_avg', 'rating_last_updated']
    list_filter = ['level']

admin.site.register(Subscription, SubscriptionAdmin)

