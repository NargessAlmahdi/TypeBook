from django import forms
from .models import Rate

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['rating', 'note']
        widgets = {
            'rating': forms.Select(attrs={
                'class': 'form-control'
            }),
            'note': forms.Textarea(attrs={
                'placeholder': 'Write your ideas...',
                'rows': 3,
                'class': 'form-control'
            }),
        }