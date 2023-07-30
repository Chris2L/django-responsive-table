from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template

class TableConsumer(WebsocketConsumer):
    def connect(self):
        self.GROUP_NAME = 'table-notification'
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )
        # Called when the socket closes

    def receive(self, text_data=None, bytes_data=None):
        self.send(text_data="Hello world!")

    def row_created(self, event):
        html = get_template("partials/row.html").render(context={
            "author": event["data"],
            "adding": True
            })
        print(f"Sending the following html\n{html}")
        self.send(text_data=html)

    def row_updated(self, event):
        html = get_template("partials/row.html").render(context={
            "author": event["data"],
            "swapping": True
            })
        print(f"Sending the following html\n{html}")
        self.send(text_data=html)
        
