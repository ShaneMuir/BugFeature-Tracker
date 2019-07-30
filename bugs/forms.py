from django import forms
from .models import BugComment

class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ('comment',)
        comment = forms.Textarea()