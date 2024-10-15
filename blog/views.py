# blog/views.py
# views to show the blog application 
from django.shortcuts import render

# Create your views here.
from . models import *
from django.views.generic import ListView, DetailView
import random

class ShowAllView(ListView):
    '''A view to show all Articles'''

    model = Article
    template_name = 'blog/show_all.html'
    context_object_name = 'articles'

class RandomArticleView(DetailView):
    '''Show one article selcted at random'''

    model = Article
    template_name = 'blog/article.html'
    context_object_name = "article"

    def get_obejct(self):
        '''Return the intstance of the Aritcel obejct to show.'''

        all_articles = Article.objects.all()

        return random.choice(all_articles)