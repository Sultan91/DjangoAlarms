from rest_framework import routers
from .api import AlarmClockViewSet, FutureAlarmClockViewSet

router = routers.DefaultRouter()
router.register('api/alarm_clocks', AlarmClockViewSet, 'Alarm clocks')
router.register('api/active_clocks', FutureAlarmClockViewSet, 'Active clocks')
urlpatterns = router.urls