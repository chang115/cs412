## mini_fb/urls.py
## description: the app-specific URLS for the mini_fb application

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [

    path(r'', views.ShowAllProfilesView.as_view(), name="show_all_profiles"),
]