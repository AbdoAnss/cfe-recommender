import csv
import random

from pprint import pprint
from django.conf import settings
from faker import Faker

SUBSCRIPTIONS_METADATA_CSV = settings.DATA_DIR / 'subscriptions_metadata.csv'



def load_subscriptions_metadata():
    with open(SUBSCRIPTIONS_METADATA_CSV, mode='r', newline='') as f:
        reader = csv.DictReader(f)
        dataset = []
        for row in reader:
            _id = row.get('id')
            try:
                _id = int(_id)
            except:
                _id = None

            data = {
                "id": _id,
                "title": row.get('title'),
                "description": row.get('description'),
                "level": row.get('level'),
            }
            
            dataset.append(data)
        return dataset

    


def get_fake_profiles(count=10):
    fake = Faker('fr_FR')
    user_data = []
    for _ in range(count):
        profile = fake.profile()
        data = {
            "username": profile.get('username'),
            "email": profile.get('mail'),
            "password": f"{profile.get('username')}@123",
            # "address": profile.get('address'),
            # "birthdate": profile.get('birthdate'),
            "is_active": True,
        }
        
        if 'name' in profile:
            fname, lname = profile.get('name').split(' ')[:2]
            data['first_name'] = fname
            data['last_name'] = lname

        user_data.append(data)
    return user_data
