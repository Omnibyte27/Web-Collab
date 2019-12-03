#from channels.routing import ProtocolTypeRouter

##url(r"^(?P<username>[\w.@+-]+)", ChatConsumer),
##url like ws://ourdomain/<username>

from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from myapp.consumers import ChatConsumer

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    
    #Wraps around websockets to ensure the host is allowed
    'websocket': AllowedHostsOriginValidator(
        #Allows/obtains access to user that is being requested
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^$", ChatConsumer),
                ]
            )
        )
    )
})