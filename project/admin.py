from django.contrib import admin

# Register your models here.
from .models import  Song, Playlist, Artist, Album
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Album)
admin.site.register(Artist)