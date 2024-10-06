## blog/urls.py
## description: the app-specific URLS for the blog application

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for this app:
urlpatterns = [
   # path(r'', views.home, name="home"), 
    path(r'', views.ShowAllView.as_view(), name="show_all"),

]