from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r"ws/tables/", consumers.TableConsumer.as_asgi()),
]