from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student

class CustomUserCreationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)  # Optional profile picture
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)  # Required field for date of birth

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'profile_picture', 'date_of_birth']
