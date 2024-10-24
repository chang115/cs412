from django.shortcuts import render
from typing import Any

# Create your views here.
from . models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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
        sm = form.save(commit=False)
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.profile = profile
        sm.profile = profile
        sm.save()
        files = self.request.FILES.getlist('files')
        for file in files:
            image = Image()
            image.image_file = file  
            image.fkey = sm  
            image.save()
        
        return super().form_valid(form)   
    
    def get_success_url(self) -> str:
    
        #return "/blog/show_all"
        #return reverse("show_all")
        return reverse("show_profile", kwargs=self.kwargs)
    
class UpdateProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def form_valid(self, form):
        
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')
        return super().form_valid(form)
    
class DeleteStatusMessageView(DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'delete_message'

    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''
        
        pk = self.kwargs.get('pk')
        message = StatusMessage.objects.filter(pk=pk).first() 
        profile = message.profile 
        return reverse('show_profile', kwargs={'pk':profile.pk})
    
class UpdateStatusMessageView(UpdateView):
    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'update_message'
    

    def form_valid(self, form):
        
        print(f'UpdateStatusMessageView: form.cleaned_data={form.cleaned_data}')
        return super().form_valid(form)
    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the update.'''
        
        pk = self.kwargs.get('pk')
        message = StatusMessage.objects.filter(pk=pk).first() 
        profile = message.profile 
        return reverse('show_profile', kwargs={'pk':profile.pk})