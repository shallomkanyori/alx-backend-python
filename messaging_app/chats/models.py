from django.db import models
from django.contrib.auth.models.AbstractBaseUser import AbstractBaseUser

class User(AbstractBaseUser):
    user_id = models.UUIDField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    password_hash = models.CharField(max_length=100, blank=False)
    phone_number = models.CharField(max_length=100, blank=True)

    role_choices = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=100, choices=role_choices, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, editable=False)
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField(blank=False)
    sent_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, editable=False)
    participants_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)