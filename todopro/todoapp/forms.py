from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['heading', 'details']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description']

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(label=_('Email'), max_length=255, widget=forms.EmailInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'username' field and use 'email' instead
        self.fields['username'].widget = self.fields['email'].widget
        self.fields['username'].label = self.fields['email'].label
        self.fields['username'].help_text = self.fields['email'].help_text
        self.fields['username'].max_length = self.fields['email'].max_length
        del self.fields['email']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name']