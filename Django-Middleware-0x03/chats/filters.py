from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.FilterSet):
    """retrieve conversations with specific users or messages within a time range"""
    created_at = filters.DateFromToRangeFilter()
    sender_id = filters.UUIDFilter()

    class Meta:
        model = Message
        fields = ['created_at', 'sender_id']