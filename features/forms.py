from django import forms
from .models import FeatureComment, Feature

class FeatureCommentForm(forms.ModelForm):
    class Meta:
        model = FeatureComment
        fields = ('comment',)
        
class FeatureCreationForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = ('title', 'description')