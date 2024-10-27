from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email = models.TextField(blank=False)
    address = models.TextField(blank=False)
    profile_image_url = models.URLField(blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_status_messages(self):

        messages = StatusMessage.objects.filter(profile=self)
        return messages

    def get_absolute_url(self) -> str:
        return reverse('show_profile', args=[self.pk])
    
    def get_friends(self):
        friendprof1 = Friend.objects.filter(profile1=self).values_list("profile2", flat=True)
        friendprof2 = Friend.objects.filter(profile2=self).values_list("profile1", flat=True)

        friendIds = list(friendprof1) + list(friendprof2)
        friendProfiles = Profile.objects.filter(id__in=friendIds)
        return list(friendProfiles)
    
    def add_friend(self, other):
        if self == other:
            return None
        
        exists = Friend.objects.filter(profile1=self, profile2=other).exists() | Friend.objects.filter(profile1=other, profile2=self).exists()
        if not exists:
            Friend.objects.create(profile1=self, profile2=other)

    def get_friend_suggestions(self):
        current_friends = self.get_friends()
        friends_ids = [friend.id for friend in current_friends]

        suggestions = Profile.objects.exclude(id__in=friends_ids) & Profile.objects.exclude(id=self.id)
        return suggestions
    
    def get_news_feed(self):
        friends = self.get_friends()
        friends_ids = [friend.id for friend in friends]

        status_messages = StatusMessage.objects.filter(profile=self).order_by('-timestamp') | StatusMessage.objects.filter(profile__in=friends).order_by('-timestamp')
        return status_messages

    
class StatusMessage(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'{self.message}'   
    
    def get_images(self):
        images = Image.objects.filter(fkey=self)
        return images

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/')
    fkey = models.ForeignKey("StatusMessage", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Image for {self.fkey.message}"
    
class Friend(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    profile1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='profile1')
    profile2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name='profile2')

    def __str__(self):
        return f"{self.profile1}" + " & " + f"{self.profile2}"