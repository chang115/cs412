from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    title = models.TextField(blank=False)
    duration = models.TextField(blank=False)
    genre = models.TextField(blank=False)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
   

    def __str__(self):
        return f"{self.title} {self.artist}"


class Playlist(models.Model):
    title = models.TextField(blank=False)
    numSongs = models.IntegerField(blank=True, null=True, default=0)
    songs = models.ManyToManyField("Song", blank=True, related_name="playlists")

    def add_song(self, song):
        """
        Adds a song to the playlist.
        """
        if song not in self.songs.all():
            self.songs.add(song)
            self.numSongs = self.songs.count()
            self.save()
            return True  # Song added successfully
        return False  # Song already in playlist
    
    def remove_song(self, song):
        """
        Removes a song from the playlist.
        """
        if song in self.songs.all():
            self.songs.remove(song)
            self.numSongs = self.songs.count()  # Update the song count
            self.save()
            return True
        return False  # Song is not in the playlist
    
    def save(self, *args, **kwargs):
        # Automatically update numSongs before saving if needed
        if self.pk:  # Only if the playlist already exists
            self.numSongs = self.songs.count()
        else:
            # For newly created playlists with no songs yet
            self.numSongs = 0
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.title}"
    

class Album(models.Model):
    title = models.TextField(blank=False)
    numSongs = models.IntegerField(blank=False)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    songs = models.ManyToManyField("Song", blank=True, related_name="albums")

    def __str__(self):
        return f"{self.title}"


class Artist(models.Model):
    fname = models.TextField(blank=False)
    lname = models.TextField(blank=False)
    stageName = models.TextField(blank=False)
    age = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.stageName}"