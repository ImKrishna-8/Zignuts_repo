"""
ASGI config for PizzaHub project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PizzaHub.settings')
from pizzaservice.consumer import PizzaUpdates
application = get_asgi_application()

ws_patterns = [
    path('ws/pizza/<order_id>/',PizzaUpdates.as_asgi())
]

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(ws_patterns),
})

