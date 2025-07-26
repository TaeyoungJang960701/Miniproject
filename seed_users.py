# seed_users.py
import os
import django
import random
from faker import Faker
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HRlist.settings')  # 프로젝트 이름
django.setup()

from HRapp.models import User

fake = Faker('ko_KR')
password_hash = 'pbkdf2_sha256$260000$fakepasswordhash'

for _ in range(50):
    birthdate = fake.date_of_birth(minimum_age=20, maximum_age=60)
    User.objects.create(
        user_email=fake.unique.email(),
        user_password=password_hash,
        user_name=fake.name(),
        user_birthdate=birthdate,
        user_phone=fake.phone_number(),
        user_address=fake.address(),
        created_at=timezone.now() - timedelta(days=random.randint(1, 100)),
        updated_at=timezone.now(),
    )
