"""
WSGI config for bimcom project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
from pathlib import Path
import os
from whitenoise import WhiteNoise

BASE_DIR = Path(__file__).resolve().parent.parent
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bimcom.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'asset'))


