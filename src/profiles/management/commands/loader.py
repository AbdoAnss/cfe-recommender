from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model

from cfehome import utils as cfehome_utils
from subscriptions.models import Subscription



User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=10,type=int)
        parser.add_argument('--subscriptions', action='store_true', default=False)
        parser.add_argument('--users', action='store_true', default=False)
        parser.add_argument('--show-total', action='store_true', help='Show total users in the database', default=False)
     



    def handle(self, *args, **options):
        count = options.get('count')
        show_total = options.get('show_total')
        load_susbcriptions = options.get('subscriptions')
        generate_users = options.get('users')
        if load_susbcriptions:
            subscriptions_dataset = cfehome_utils.load_subscriptions_metadata()
            new_subs = []
            for sub in subscriptions_dataset:
                new_subs.append(Subscription(**sub))
            sub_bulk = Subscription.objects.bulk_create(new_subs)
            self.stdout.write(self.style.SUCCESS(f"Created {len(sub_bulk)} new subscriptions items"))
            if show_total:
                self.stdout.write(self.style.SUCCESS(f"Total subscription items in the database: {Subscription.objects.count()}"))
            

        if generate_users:
            profiles = cfehome_utils.get_fake_profiles(count=count)
            new_users = []
            for profile in profiles:
                new_users.append(User(**profile))
            user_bulk = User.objects.bulk_create(new_users)
            self.stdout.write(self.style.SUCCESS(f"Created {len(user_bulk)} new users"))
            if show_total:
                self.stdout.write(self.style.SUCCESS(f"Total users in the database: {User.objects.count()}"))




