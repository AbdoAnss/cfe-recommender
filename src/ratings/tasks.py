import random

from celery import shared_task

from profiles.models import UserProfile
from django.contrib.auth import get_user_model
from subscriptions.models import Subscription
from .models import Rating, RatingChoices

User = get_user_model()



@shared_task(name='generate_fake_reviews')
def generate_fake_reviews(users=10):
    user_s = UserProfile.objects.first()
    user_e = UserProfile.objects.last()

    random_user_id = random.sample(range(user_s.user.id, user_e.user.id), users)

    users = UserProfile.objects.filter(user__id__in=random_user_id).all()
    subscriptions = Subscription.objects.all()

    # rating_choices = [1, 2, 3, 4, 5] #this is ok, but we can also use the RatingChoices class
    # rating_choices = [RatingChoices.ONE, RatingChoices.TWO, RatingChoices.THREE, RatingChoices.FOUR, RatingChoices.FIVE]
    # or more generally
    # rating_choices = [x for x in RatingChoices if x is not None]
    rating_choices = [choice for choice, _ in RatingChoices.choices if choice is not None]


    new_ratings = []

    for user in users:
        if user.coverage_type==4:
            for subscription in subscriptions:
                rating = Rating.objects.create(
                    content_object=subscription,
                    user=user.user,
                    value=random.choice(rating_choices)
                )
                new_ratings.append(rating)
        elif user.coverage_type==3:
            possible_subscriptions = subscriptions.filter(id__lt=400)
            for subscription in possible_subscriptions:
                rating = Rating.objects.create(
                    content_object=subscription,
                    user=user.user,
                    value=random.choice(rating_choices)
                )
                new_ratings.append(rating)
        elif user.coverage_type==2:
            possible_subscriptions = subscriptions.filter(id__lt=300)
            for subscription in possible_subscriptions:
                rating = Rating.objects.create(
                    content_object=subscription,
                    user=user.user,
                    value=random.choice(rating_choices)
                )
                new_ratings.append(rating)
        elif user.coverage_type==1:
            possible_subscriptions = subscriptions.filter(id__lt=200)
            for subscription in possible_subscriptions:
                rating = Rating.objects.create(
                    content_object=subscription,
                    user=user.user,
                    value=random.choice(rating_choices)
                )
                new_ratings.append(rating)
        else:
            continue
    return new_ratings