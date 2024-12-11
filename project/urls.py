## project/urls.py
## description: the app-specific URLS for the quotes application

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLS for this app:
urlpatterns = [
    path(r'', views.HomeView.as_view(), name="homepage"),
    path(r'jam', views.SongListView.as_view(), name="search"),
    path(r'playlists', views.PlaylistListView.as_view(), name="playlists"),
    path(r'song/<int:pk>', views.SongDetailView.as_view(), name="song_detail"),
    path(r'playlist/<int:pk>', views.PlaylistDetailView.as_view(), name="playlist_detail"),
    path(r'album/<int:pk>', views.AlbumDetailView.as_view(), name="album_detail"),
    path(r'artist/<int:pk>', views.ArtistDetailView.as_view(), name="artist_detail"),
    path(r'playlist/create/', views.PlaylistCreateView.as_view(), name='playlist_create'),
    path(r'playlist/<int:pk>/delete/', views.PlaylistDeleteView.as_view(), name='playlist_delete'),
    path(r'playlist/<int:pk>/edit/', views.PlaylistUpdateView.as_view(), name='playlist_update'),
]   