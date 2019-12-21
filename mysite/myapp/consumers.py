import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Input

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        #When the websocket connects
        print("Connected", event)

        me = self.scope['user']

        chat_room = "main_chat"
        self.chat_room = chat_room
        #Creates the chatroom
        await self.channel_layer.group_add(
            chat_room,
            #Adding current user's channel to the unique name of that chatroom
            self.channel_name
        )

        await self.send({
            "type":"websocket.accept"
        })

    async def websocket_receive(self, event):
        #When the websocket receives something and should respond
        print("Receive", event)

        #Grab the front-end text
        front_text = event.get('text', None) #Grabs the string/key of text or None
        #Means the key exists
        if front_text is not None:
            #Load the data - Gives the actual dictionary
            loaded_dict_data = json.loads(front_text)
            #Get the message
            msg = loaded_dict_data.get('message')
            print(msg)

            #Send dictionary to client
            user = self.scope['user']
            username = 'default'
            if user.is_authenticated:
                username = user.username
                await self.create_message(msg, user)
            myResponse = { #Response is still going through, but being triggered in
            #a different place now (by chat_message)
                'message': msg,
                'username': username
            }

            #Broadcasts the message event to be sent - trigger the chat_message
            #function for all group members
            await self.channel_layer.group_send(
                #Where it will be sent - to chatroom, created when connected
                self.chat_room,
                #Event to be sent - send through new event
                {
                    "type": "chat_message",
                    #"message": "Hello world"
                    "text": json.dumps(myResponse)
                }
            )

    #Method that sends out websocket, not related to the web socket
    async def chat_message(self, event):
        #Sends the actual message
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        #When the websocket disconnects
        print("Disconnected", event)

        #raise channels.exceptions.StopConsumer()
    
        await self.send({
            ##Closing the socket connection from the backend
            "type":"websocket.close"
        })

    @database_sync_to_async
    def create_message(self, msg, username):
        return Input.objects.create(input=msg, author=username)
        