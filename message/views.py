# from django.shortcuts import render
# from django.views import generic

# # Create your views here.
# class Chat(generic.TemplateView):
#     template_name = "message/chat.html"

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Messages
from .forms import MessageForm

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
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'message/inbox.html', {'messages': messages})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id, recipient=request.user)
    message.is_read = True  
    message.save()
    return render(request, 'message/message_detail.html', {'message': message})
