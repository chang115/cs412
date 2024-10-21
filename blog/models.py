# blog/models.py
# Define data models (objects0 for use in the blog applicaiton)
from django.db import models

# Create your models here.
class Article(models.Model):
    '''Encapsulate  the dat afor a blog Aritcle by some author.'''
    #data attributes:
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    #image_url = models.URLField(blank=True) ## new field
    image_file = models.ImageField(blank=True)

    def __str__(self):
        '''Return a string representation of this Article'''
        return f"{self.title} by {self.author}"
    
    #when u need to run migrations only when you modify the data
    