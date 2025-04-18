import os

import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from config.env import env


os.environ.setdefault("DJANGO_SETTINGS_MODULE", env("DJANGO_SETTINGS_MODULE"))
django.setup()

application = application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
    }
)
