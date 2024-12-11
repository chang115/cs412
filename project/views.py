## project/views.py
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import *
from django.db.models import Q
from django.urls import reverse

# Create your views here.

class HomeView(ListView):
    template_name = 'project/home.html'
    model = Song
    context_object_name = 'songs'

class SongListView(ListView):
    template_name = 'project/search.html'
    model = Song
    context_object_name = 'songs'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query', '')
        print(f"Query: '{query}'") 

        if query:
            # Search in title, artist's stage name, album title
            queryset = queryset.filter(
                Q(title__icontains=query) |  # Match song title
                Q(artist__stageName__icontains=query) |  # Match artist's stage name
                Q(album__title__icontains=query) |  # Match album title
                Q(genre__icontains=query) # Match genre
            )

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SongSearchForm(self.request.GET or None)  # Add the search form to the context
        return context
    

class SongDetailView(DetailView):
    template_name = 'project/song_detail.html'
    model = Song
    context_object_name = 'song'


# Playlist Views
class PlaylistListView(ListView):
    model = Playlist
    template_name = 'project/playlist.html'
    context_object_name = 'playlists'


class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'project/playlist_detail.html'
    context_object_name = 'playlist'


class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = CreatePlaylistForm
    template_name = 'project/playlist_form.html'

    def get_success_url(self):
        # Redirect to a page that shows the newly created playlist’s details
        return reverse('playlist_detail', kwargs={'pk': self.object.pk})


class PlaylistUpdateView(UpdateView):
    model = Playlist
    form_class = UpdatePlaylistForm
    template_name = 'project/playlist_form.html'

    def get_success_url(self):
        # Redirect to a detail page or list page after successful update
        return reverse('playlist_detail', kwargs={'pk': self.object.pk})


class PlaylistDeleteView(DeleteView):
    model = Playlist
    template_name = 'project/playlist_confirm_delete.html'
    context_object_name = 'delete_playlist'
   
    def get_success_url(self):
        return reverse('playlists')
    
# Album Views

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'project/album_detail.html'
    context_object_name = 'album'

# Artist Views

class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'project/artist_detail.html'
    context_object_name = 'artist'



