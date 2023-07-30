from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template
import json

from .forms import AuthorForm
from .models import Author

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
        data = json.loads(text_data)
        kwargs = {}
        for d in data:
            if "HEADERS" in d:
                break
            prop, id = d.split("-")
            kwargs["id"] = int(id)
            kwargs[prop] = data[d]
        print(kwargs)

        try:
            inst = Author.objects.get(id=kwargs["id"])
            for arg in kwargs:
                print(f"{arg} - {kwargs[arg]}")
                
                setattr(inst, arg, True if kwargs[arg] == "on" else kwargs[arg] )
            inst.save()
            print("This should be an update")
        except:
            form = AuthorForm(kwargs)
            print("This should be an add")


    def row_created(self, event):
        html = get_template("partials/row.html").render(context={
            "author": event["data"],
            "adding": True
            })
        self.send(text_data=html)

    def row_updated(self, event):
        html = get_template("partials/row.html").render(context={
            "author": event["data"],
            "swapping": True
            })
        self.send(text_data=html)

    def row_deleted(self, event):
        html = get_template("partials/row.html").render(context={
            "author": event["data"],
            "removing": True
            })
        self.send(text_data=html)
        
