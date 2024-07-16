from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from profiles.models import UserProfile
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate coverage_type field with random integers between 1 and 4 for each user'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            profile, created = UserProfile.objects.get_or_create(user=user)
            profile.coverage_type = random.randint(1, 4)
            profile.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated coverage_type for all users'))
