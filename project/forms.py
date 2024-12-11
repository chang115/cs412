# forms.py
from django import forms
from .models import Playlist, Song

class SongSearchForm(forms.Form):
    query = forms.CharField(label='Search Songs', max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter song title, artist, or album',
            'class': 'form-control',
        }))
    
class CreatePlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['title']
    
class UpdatePlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['title', 'songs']


