"""
ASGI config for studentGenerate project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from student.consumer import Test 
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentGenerate.settings')

ws_patterns = [
   path('ws/test/', Test.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket':URLRouter(ws_patterns),
    'http':get_asgi_application()
})