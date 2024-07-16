from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model


from subscriptions.tasks import task_calculate_subscription_rating




User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=1_000,type=int)
        parser.add_argument('--all', action='store_true', help='do all calculations', default=False)

    def handle(self, *args, **options):
        count = options.get('count')
        all = options.get('all')
        task_calculate_subscription_rating(all=all, count=count)


     