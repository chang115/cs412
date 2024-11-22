from django.contrib import admin

# Register your models here.
from .models import Account, Song, Playlist, Artist, Album
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(Album)
admin.site.register(Account)
admin.site.register(Artist)