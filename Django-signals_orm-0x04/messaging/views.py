from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from .serializers import MessageSerializer, MessageHistorySerializer, NotificationSerializer, UserSerializer
from .models import Message, MessageHistory, Notification
from django.db.models import Q
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

@api_view(['DELETE'])
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class MessageViewSet(viewsets.ViewSet):
    queryset = Message.objects.filter(Q(sender_id=request.user.user_id) | Q(receiver_id=request.user.user_id))

    def list(self, request):
        serializer = MessageSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        message = get_object_or_404(self.queryset, pk=pk)
        history = MessageHistory.objects.filter(message=message)

        serializer = MessageSerializer(message)
        history_serializer = MessageHistorySerializer(history, many=True)

        response_data = serializer.data
        response_data['history'] = history_serializer.data

        return Response(response_data)

class NotificationViewSet(viewsets.ViewSet):
    queryset = Notification.objects.filter(receiver_id=request.user.user_id)

    def list(self, request):
        serializer = NotificationSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        notification = get_object_or_404(self.queryset, pk=pk)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

class MessageHistoryViewSet(viewsets.ViewSet):
    queryset = MessageHistory.objects.all()

    def list(self, request):
        serializer = MessageHistorySerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        history = get_object_or_404(self.queryset, pk=pk)
        serializer = MessageHistorySerializer(history)
        return Response(serializer.data)