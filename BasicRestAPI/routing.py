from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from django.conf.urls import url
from notifier.consumers import AlarmConsumer
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

application = ProtocolTypeRouter({
  #  "websocket": URLRouter([
  #      path("notifications/", AlarmConsumer),
  #  ])
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url('listen_alarm', AlarmConsumer)
                ]
            )
        )
    )
})