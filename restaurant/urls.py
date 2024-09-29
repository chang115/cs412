## restaurant/urls.py
## description: the app-specific URLS for the quotes application

from django.urls import path
from django.conf import settings
from . import views

# create a list of URLs for this app:
urlpatterns = [
    path(r'', views.restaurant, name="restaurant"), 
    path(r'order', views.order, name="order"), ## new
    path(r'confirmation', views.confirmation, name="confirmation"),
]