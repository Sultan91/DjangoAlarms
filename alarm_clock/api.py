from alarm_clock.models import AlarmClock
from rest_framework import viewsets, permissions
from .serializers import AlarmClockSerializer
from datetime import datetime



# Creating Lead viewset
class AlarmClockViewSet(viewsets.ModelViewSet):
    queryset = AlarmClock.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AlarmClockSerializer


class FutureAlarmClockViewSet(viewsets.ModelViewSet):
    queryset = AlarmClock.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    def get_queryset(self):
        queryset = AlarmClock.objects.all()
        cur_time = datetime.now()
        print(cur_time.time())

        if cur_time is not None:
            queryset = queryset.filter(alarm_time__gt=cur_time).order_by('alarm_time')
        return queryset

    serializer_class = AlarmClockSerializer



