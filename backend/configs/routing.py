from channels.routing import URLRouter

from django.urls import path

from apps.chat.routing import websocket_urlpatterns as chat_routing
from apps.task.routing import websocket_urlpatterns as task_routing

websocket_urlpatterns = [
    path('api/chat/', URLRouter(chat_routing)),
    path('api/tasks', URLRouter(task_routing)),
]
