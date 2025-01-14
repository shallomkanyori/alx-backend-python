from rest_framework import permissions
from .models import Conversation

class IsParticipantOfConversation(permissions.BasePermission):
    """Custom permission class to allow only participants of a conversation to access it."""

    def has_permission(self, request, view):
        conversation_id = view.kwargs.get('conversation_pk')
        if conversation_id:
            conversation = Conversation.objects.filter(conversation_id=conversation_id).first()
            return conversation and request.user in conversation.participants.all()
        return True

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Conversation):
            return request.user in obj.participants.all()
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user == obj.sender_id