from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """Custom permission class to allow only participants of a conversation to access it."""

    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()