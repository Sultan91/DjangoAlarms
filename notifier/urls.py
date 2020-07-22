from django.urls import path

from notifier.views import home_view

urlpatterns = [
    path('', home_view),
]