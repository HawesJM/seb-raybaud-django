from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.urls import reverse
from .models import ContactMessage
from .forms import ContactMessageForm

# Create your views here.
def send_message(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            form = ContactMessageForm()  # Reset the form after saving
            return redirect(reverse('send_message'))
        else:
            messages.error(request, 'There was an error sending your message. Please try again.')
    else:
        form = ContactMessageForm()
    template = 'contact/contact_me.html'
    context = {
        'form': form,
    }

    return render(request, template, context)