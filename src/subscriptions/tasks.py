from celery import shared_task

from .models import Subscription


@shared_task(name='task_calculate_subscription_rating')
def task_calculate_subscription_rating(all=False, count=None):
    qs = Subscription.objects.needs_updating()
    if all:
        qs = Subscription.objects.all()

    qs = qs.order_by('rating_last_updated')

    if isinstance(count, int):
        qs = qs[:count]
    for obj in qs:
        obj.calculate_rating(save=True)