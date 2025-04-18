from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from config.env import env


class Command(BaseCommand):
    help = "Create a superuser with all required fields and password"

    def handle(self, *args, **options):
        User = get_user_model()

        phone = env("DJANGO_SUPERUSER_PHONE")
        password = env("DJANGO_SUPERUSER_PASSWORD")
        first_name = "Admin"
        last_name = "User"

        if not phone or not password:
            self.stdout.write(
                self.style.ERROR("Missing required environment variables")
            )
            return

        if User.objects.filter(phone=phone).exists():
            self.stdout.write(self.style.WARNING("Superuser already exists"))
        else:
            User.objects.create_superuser(
                phone=phone,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
