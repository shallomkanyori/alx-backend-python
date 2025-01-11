from django.db import models
import uuid

class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    receiver = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.message} - {self.edited_at}'

class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    receiver = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.message} - {self.receiver}'