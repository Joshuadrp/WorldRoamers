from django import forms
from .models import Messages

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['recipient', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your message here...'}),
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['content']  # Only the content of the reply is needed
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your reply here...'
            })
        }
