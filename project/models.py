from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    title = models.TextField(blank=False)
    duration = models.TextField(blank=False)
    genre = models.TextField(blank=False)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)
    playlist = models.ForeignKey("Playlist", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.artist}"


class Playlist(models.Model):
    title = models.TextField(blank=False)
    numSongs = models.IntegerField(blank=False)
    account = models.ForeignKey("Account", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.account}"
    

class Album(models.Model):
    title = models.TextField(blank=False)
    numSongs = models.IntegerField(blank=False)
    artist = models.ForeignKey("Artist", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.artist}"


class Account(models.Model):
    fname = models.TextField(blank=False)
    lname = models.TextField(blank=False)
    dob = models.DateField(blank=False)
    email = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fname} {self.lname}"


class Artist(models.Model):
    fname = models.TextField(blank=False)
    lname = models.TextField(blank=False)
    stageName = models.TextField(blank=False)
    age = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.stageName} "