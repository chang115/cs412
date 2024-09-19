## hw/views.py
## description: the logic to handle URL requests
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

# Create your views here.

def home(request):
    '''
    Function to handle the URL request for /hw (home page).
    Delegate rendering to the template hw/home.html
    '''

    template_name = 'hw/home.html'

    context = {
        "current_time" : time.ctime(),
        "letter1" : chr(random.randint(65, 90)),
        "letter2" : chr(random.randint(65, 90)),
        'number' : random.randint(1, 10),
    }

    #delegate response to the template
    return render(request, template_name, context)

def about(request):
    '''
    A function to respond to the /hw/about URL.
    This function will delegate work to an HTML template.
    '''
    # this template will present the response
    template_name = "hw/about.html"

    # create a dictionary of context variables
    context = {
        'current_time': time.ctime(),
    }

    # delegate response to the template:
    return render(request, template_name, context)