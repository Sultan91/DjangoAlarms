from channels.generic.websocket import AsyncConsumer
from alarm_clock.models import AlarmClock
from django.core import serializers
from channels.db import database_sync_to_async
import datetime


class AlarmConsumer(AsyncConsumer):
    @database_sync_to_async
    def get_running_alarms(self):
        alarm_clocks = AlarmClock.objects.all()
        cur_time = datetime.datetime.now().replace(second=0, microsecond=0)
        cur_time = cur_time.time()
        print("CURRENT TIME", cur_time)
        alarm_clocks = alarm_clocks.filter(alarm_time=cur_time).order_by('title')
        alarm_clocks_json = serializers.serialize('json', alarm_clocks)
        return alarm_clocks_json

    async def websocket_connect(self, event):
        alarm_clocks_json = await self.get_running_alarms()
        print("CONNECTED", event)
        print(alarm_clocks_json)
        await self.send({
            "type": "websocket.accept"
        })
        await self.send({
            "type": "websocket.send",
            "text": alarm_clocks_json
        })

    async def websocket_receive(self, event):
        print("RECEIVE", event)

    async def websocket_disconnect(self, event):
        print("DISCONNECTED", event)