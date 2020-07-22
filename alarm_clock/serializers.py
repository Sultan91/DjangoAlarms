from rest_framework import serializers
from alarm_clock.models import AlarmClock
# AlarmClock serializer


class AlarmClockSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlarmClock
        fields = '__all__'