from .view import MessageViewSet, NotificationViewSet, MessageHistoryViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'messages', MessageViewSet, basename='messages')
router.register(r'notifications', NotificationViewSet, basename='notifications')
router.register(r'message-history', MessageHistoryViewSet, basename='message-history')

urlpatterns = [
    path('', include(router.urls)),
]