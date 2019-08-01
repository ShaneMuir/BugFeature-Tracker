from django import forms
from .models import BugComment, Bug

class BugCommentForm(forms.ModelForm):
    class Meta:
        model = BugComment
        fields = ('comment',)
        
class BugCreationForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description')