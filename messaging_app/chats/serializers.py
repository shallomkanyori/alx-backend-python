from rest_framework import serializers
from .models import  User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    first_name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'full_name', 'email', 'role', 'phone_number', 'created_at']
    
    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'sender_id', 'conversation_id', 'message_body', 'sent_at']
    
    def validate_message_body(self, message_body):
        if len(message_body.strip()) == 0:
            raise serializers.ValidationError('Message body cannot be empty')
        return message_body
    
class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants_id', 'created_at', 'messages']