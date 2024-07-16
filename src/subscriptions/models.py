import datetime

from ratings.models import Rating
from django.utils import timezone
from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericRelation


# Create your models here.

RATING_CALC_TIME_DAYS = 3


class SubscriptionQuerySet(models.QuerySet):
    def needs_updating(self):
        now = timezone.now()
        days_ago = now - datetime.timedelta(days=RATING_CALC_TIME_DAYS)
        return self.filter(
            Q(rating_last_updated__isnull=True)|
            Q(rating_last_updated__lte=days_ago)
        )



class SubscriptionManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return SubscriptionQuerySet(self.model, using=self._db)
    
    def needs_updating(self):
        return self.get_queryset().needs_updating()


class Subscription(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    level = models.CharField(max_length=120)
    ratings = GenericRelation(Rating) # new queryset
    rating_last_updated = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)
    rating_avg = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)

    objects = SubscriptionManager()

    def get_absolute_url(self):
        return f"/subscriptions/{self.id}/"
    
    def __str__(self):
        return f"{self.title} ({self.level})"
    



    # only update the rating if it has been more than 4 hours 
    def rating_avg_display(self):
        now = timezone.now()

        if not self.rating_last_updated:
            return self.calculate_rating()
        if self.rating_last_updated:
            time_diff = now - self.rating_last_updated
            if time_diff < datetime.timedelta(days=RATING_CALC_TIME_DAYS):
                return self.rating_avg
        return self.calculate_rating()

    def calculate_rating_count(self):
        return self.ratings.all().count()

    def calculate_rating_avg(self):
        return self.ratings.all().avg()
    
    def calculate_rating(self, save = True):
        rating_avg = self.calculate_rating_avg()
        rating_count = self.calculate_rating_count()
        self.rating_avg = rating_avg
        self.rating_count = rating_count
        self.rating_last_updated = timezone.now()
        if save:
            self.save()
        return rating_avg

      
