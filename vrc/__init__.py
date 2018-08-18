from .client import VRChatClient

from django.conf import settings

vrc_client = VRChatClient(
    username=settings.VRC_USERNAME,
    password=settings.VRC_PASSWORD)
