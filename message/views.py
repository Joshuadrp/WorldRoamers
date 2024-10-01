# from django.shortcuts import render
# from django.views import generic

# # Create your views here.
# class Chat(generic.TemplateView):
#     template_name = "message/chat.html"

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from .models import Messages
from .forms import MessageForm
from django.db.models import Q
from django import forms

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('inbox')  
    else:
        form = MessageForm()
    return render(request, 'message/send_message.html', {'form': form})

@login_required
def inbox(request):
    messages = Messages.objects.filter(recipient=request.user).order_by('-sent_on')
    return render(request, 'message/inbox.html', {'messages': messages})

@login_required
def message_detail(request, message_id):
    original_message = get_object_or_404(Messages, id=message_id)
    chat_messages = Messages.objects.filter(
        Q(sender=request.user, recipient=original_message.sender) |
        Q(sender=original_message.sender, recipient=request.user)
    ).order_by('sent_on')
    
    if request.method == 'POST':
        reply_form = MessageForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.sender = request.user
            reply.recipient = original_message.sender if original_message.sender != request.user else original_message.recipient
            reply.parent_message = original_message
            reply.save()
            return redirect('message_detail', message_id=original_message.id) 
    else:
        reply_form = MessageForm()

    
    reply_form.fields['recipient'].widget = forms.HiddenInput()

    context = {
        'message': original_message,
        'chat_messages': chat_messages,
        'reply_form': reply_form,
    }
    return render(request, 'message/message_detail.html', context)