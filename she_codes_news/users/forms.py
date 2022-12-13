from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'bio', 'profile_picture', 'linkedin', 'instagram', 'github',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder': 'Enter your name',}),
            'username': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder':'Enter a username'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter your email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a bio'}),
            'profile_picture': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder':'Enter a URL'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a URL to your LinkedIn'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a URL to your Instagram'}),
            'github': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a URL to your GitHub'}),
            }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'email', 'bio', 'profile_picture', 'linkedin', 'instagram', 'github',]
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder': 'Enter your name',}),
            'username': forms.TextInput(attrs={'class':'form-control form-item', 'placeholder':'Enter a username'}),
            'email': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter your email'}),
            'bio': forms.Textarea(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a bio'}),
            'profile_picture': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder':'Enter a URL'}),
            'linkedin': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a URL to your LinkedIn'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a URL to your Instagram'}),
            'github': forms.TextInput(attrs={'class': 'form-control form-item', 'placeholder': 'Enter a URL to your GitHub'}),
            }

# Django has inherent properties for UserCreationForm and UserChange Form, creating Custom users allows us to make changes to things that already exist