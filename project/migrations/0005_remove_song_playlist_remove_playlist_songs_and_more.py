# Generated by Django 5.1.1 on 2024-12-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_remove_playlist_songs_playlist_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='playlist',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='songs',
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='playlists', to='project.song'),
        ),
    ]