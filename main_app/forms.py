from django import forms
from .models import Rating, Note

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        widgets = {
            'rating': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']
        widgets = {
            'note': forms.Textarea(attrs={
                'placeholder': 'Write your ideas...',
                'rows': 3,
                'class': 'form-control'
            }),
        }
