from django.shortcuts import render, redirect
from typing import Any

# Create your views here.
from . models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin ## NEW
from django.contrib.auth.forms import UserCreationForm




class ShowAllProfilesView(ListView):

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Add the logged-in user's profile to the context
            context['user_profile'] = Profile.objects.get(user=self.request.user)
        return context


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'show_profile'


class CreateProfileView(CreateView):
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_context_data(self, **kwargs:Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        userform = UserCreationForm()
        context['userform'] = userform
        return context
    
    def form_valid(self, form):
        
        user_form = UserCreationForm(self.request.POST)
        
        if user_form.is_valid():
            
            user = user_form.save()
            form.instance.user = user  
            
            return super().form_valid(form)
        
        return self.form_invalid(form)
        

    def get_success_url(self):
        return reverse('show_profile', kwargs={'pk': self.object.pk})


class CreateStatusMessageView(LoginRequiredMixin, CreateView):
    form_class = CreateStatusMessageForm
    template_name = 'mini_fb/create_status_form.html'

    def get_object(self):
        # Retrieve the profile associated with the logged-in user
        return Profile.objects.get(user=self.request.user)
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''
        build the template context data --
        a dict of key-value pairs.'''

        context = super().get_context_data(**kwargs)

        profile = self.get_object()
        context['profile'] = profile

        return context
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login')

    def form_valid(self, form):
        sm = form.save(commit=False)
        profile = self.get_object()
        form.instance.profile = profile
        sm.profile = profile
        sm.save()
        files = self.request.FILES.getlist('files')
        for file in files:
            image = Image()
            image.image_file = file  
            image.fkey = sm  
            image.save()
        user = self.request.user
        print(f'UpdateProfileView:form_valid() user={user}')
        form.instance.user = user        
        return super().form_valid(form)   
    
    def get_success_url(self) -> str:
    
        #return "/blog/show_all"
        #return reverse("show_all")
        return reverse("show_profile", kwargs={"pk": self.get_object().pk})
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

    def get_object(self):
        # Retrieve the profile associated with the logged-in user
        return Profile.objects.get(user=self.request.user)

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login')

    def form_valid(self, form):
        
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')
        user = self.request.user
        print(f'UpdateProfileView:form_valid() user={user}')
        form.instance.user = user
        return super().form_valid(form)
    
class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    model = StatusMessage
    template_name = 'mini_fb/delete_status_form.html'
    context_object_name = 'delete_message'

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login')
    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''
        
        pk = self.kwargs.get('pk')
        message = StatusMessage.objects.filter(pk=pk).first() 
        profile = message.profile 
        return reverse('show_profile', kwargs={'pk':profile.pk})
    
class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
    model = StatusMessage
    form_class = UpdateStatusMessageForm
    template_name = 'mini_fb/update_status_form.html'
    context_object_name = 'update_message'
    
    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login')

    def form_valid(self, form):
        
        print(f'UpdateStatusMessageView: form.cleaned_data={form.cleaned_data}')
        return super().form_valid(form)
    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the update.'''
        
        pk = self.kwargs.get('pk')
        message = StatusMessage.objects.filter(pk=pk).first() 
        profile = message.profile 
        return reverse('show_profile', kwargs={'pk':profile.pk})
    
class CreateFriendView(LoginRequiredMixin, View):

    def get_object(self):
        # Retrieve the profile associated with the logged-in user
        return Profile.objects.get(user=self.request.user)

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login')

    def dispatch(self, request, *args, **kwargs):
        #pk = kwargs.get('pk')
        other_pk = kwargs.get('other_pk')

        profile = self.get_object()
        #profile = Profile.objects.get(pk=pk)
       
        other_profile = Profile.objects.get(pk=other_pk)

        profile.add_friend(other_profile)
        
        return redirect('show_profile', pk=profile.pk)
    
class ShowFriendSuggestionsView(DetailView):
    model = Profile
    template_name = 'mini_fb/friend_suggestions.html'
    context_object_name = 'profile'

    def get_object(self):
        # Retrieve the profile associated with the logged-in user
        return Profile.objects.get(user=self.request.user)

class ShowNewsFeedView(DetailView):
    model = Profile
    template_name = 'mini_fb/news_feed.html'
    context_object_name = 'profile'

    def get_object(self):
        # Retrieve the profile associated with the logged-in user
        return Profile.objects.get(user=self.request.user)