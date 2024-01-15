import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "example.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Dev")

from configurations.asgi import get_asgi_application

application = get_asgi_application()
