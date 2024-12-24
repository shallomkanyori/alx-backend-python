from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from .serializers import ConversationSerializer, MessageSerializer
from .models import Conversation, Message
from .permissions import IsParticipantOfConversation
from rest_framework.permissions import IsAuthenticated

class ConversationViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def list(self, request):
        queryset = Conversation.objects.filter(participants__user_id=request.user.user_id)
        serializer = ConversationSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Conversation.objects.all()
        conversation = get_object_or_404(queryset, pk=pk)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    @action(detail=True, methods=['post'])
    def add_message(self, request, pk=None):
        conversation = self.get_object()
        message = request.data.get('message')
        message = Message.objects.create(conversation=conversation, message=message)
        serializer = MessageSerializer(message)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageViewSet(viewsets.ViewSet):
    def list(self, request, conversation_pk=None):
        queryset = Message.objects.filter(conversation_id=conversation_pk)
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, conversation_pk=None):
        queryset = Message.objects.filter(conversation_id=conversation_pk)
        message = get_object_or_404(queryset, pk=pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data)
    
    def create(self, request, conversation_pk=None):
        data = request.data
        data['conversation_id'] = conversation_pk
        data['sender_id'] = request.user.user_id
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk=None, conversation_pk=None):
        message = self.get_object()
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def destroy(self, request, pk=None, conversation_pk=None):
        message = self.get_object()
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)