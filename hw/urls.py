## hw/urls.py
##description: URL patterns for the hw app

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLS for this app:
urlpatterns = [
    path(r'', views.home, name="home"), ## our first URL
    path(r'about', views.about, name="about"), ## new
]