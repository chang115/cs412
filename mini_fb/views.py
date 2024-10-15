from django.shortcuts import render
from typing import Any

# Create your views here.
from . models import *
from django.views.generic import ListView, DetailView, CreateView
from .forms import *




class ShowAllProfilesView(ListView):

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'show_profile'


class CreateProfileView(CreateView):
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class CreateStatusMessageView(CreateView):
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''
        build the template context data --
        a dict of key-value pairs.'''

        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(pk=self.kwargs['pk'])

        context['profile'] = profile

        return context

    def form_valid(self, form):

        profile = Profile.objects.get(pk=self.kwargs['pk'])

        form.instance.profile = profile

        return super().form_valid(form)   
    
    def get_success_url(self) -> str:
    
        #return "/blog/show_all"
        #return reverse("show_all")
        return reverse("show_profile", kwargs=self.kwargs)
