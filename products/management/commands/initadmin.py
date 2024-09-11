import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True):
            self.stdout = 'Admin account alreqdy exists'
            return

        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        admin = User.objects.create_superuser(email=email, password=password)
        admin.is_active = True
        admin.is_admin = True
        admin.save()

        self.stdout = f'Create superuser with {email=} and {password=}'
