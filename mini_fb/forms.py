from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email', 'address', 'profile_image_url', ]

class CreateStatusMessageForm(forms.ModelForm):

    class Meta:
        model = StatusMessage
        fields = ['message']

class UpdateProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['city', 'email', 'address', 'profile_image_url']

class UpdateStatusMessageForm(forms.ModelForm):

    class Meta:
        model = StatusMessage
        fields = ['message']