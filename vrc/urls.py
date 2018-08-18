from django.urls import path

from .views import VRCView

urlpatterns = [
    path('users/', VRCView.as_view())
]