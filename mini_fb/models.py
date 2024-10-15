from django.db import models

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
    
class StatusMessage(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    message = models.TextField(blank=False)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'{self.message}'   