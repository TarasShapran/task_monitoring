from django.urls import path

from apps.task.consumers import TaskConsumer

websocket_urlpatterns = [
    path('', TaskConsumer.as_asgi()),
]
