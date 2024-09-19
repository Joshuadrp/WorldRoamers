from django import forms
from .models import Messages

class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['recipient', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Write your message here...'}),
        }
