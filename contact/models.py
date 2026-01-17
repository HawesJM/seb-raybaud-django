from django.db import models

# Create your models here.
class ContactMessage(models.Model):
    message_date = models.DateTimeField(auto_now_add=True)
    message_content = models.TextField(max_length=500)
    sender_email = models.EmailField(max_length=254)
