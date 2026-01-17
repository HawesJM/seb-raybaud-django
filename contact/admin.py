from django.contrib import admin
from .models import ContactMessage
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender_email',
        'message_date',
    )
    ordering = ('message_date',)


admin.site.register(ContactMessage, MessageAdmin)
