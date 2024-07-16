from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model


from ratings.tasks import generate_fake_reviews
from ratings.models import Rating



User = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('count', nargs='?', default=10,type=int)
        parser.add_argument('--users', default = 10, type=int)
        parser.add_argument('--show-total', action='store_true', help='Show total users in the database', default=False)

    def handle(self, *args, **options):
        count = options.get('count')
        show_total = options.get('show_total')
        user_count = options.get('users')
        new_ratings = generate_fake_reviews(users=user_count)
        self.stdout.write(self.style.SUCCESS(f"Created {len(new_ratings)} new ratings items"))
        if show_total:
            qs = Rating.objects.all()
            self.stdout.write(self.style.SUCCESS(f"Total ratings items in the database: {qs.count()}"))



     