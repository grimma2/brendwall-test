import os
import time

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


User = get_user_model()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.filter(is_superuser=True):
            self.stdout = 'Admin account already exists'
            return

        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not any((email, username, password)):
            self.stderr = '''
                Is required to create env var for superuser fields: username, email, password
            '''
            return

        admin = User.objects.create_superuser(username=username, email=email, password=password)
        admin.is_active = True
        admin.is_admin = True
        admin.save()

        self.stdout = f'Create superuser with {email=} and {password=}'
