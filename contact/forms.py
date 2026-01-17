from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['sender_email', 'message_content']
        widgets = {
            'sender_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'message_content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message', 'rows': 5}),
        }