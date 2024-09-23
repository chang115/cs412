## quotes/views.py
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import time
import random

quotesl = ["Darkness cannot drive out darkness, only light can do that. Hate cannot drive out hate, only love can do that.", 
          "Out of the mountain of despair, a stone of hope", 
          "True peace is not merely the absence of tension; it is the presence of justice."]

imagesl = ["https://upload.wikimedia.org/wikipedia/commons/0/05/Martin_Luther_King%2C_Jr..jpg",
          "https://cdn.britannica.com/18/1918-050-0166D6BB/Martin-Luther-King-Jr.jpg",
          "https://i.natgeofe.com/n/f0f3505e-a427-453f-814c-696a3831e401/06-martin-luther-king_16x9.jpg"]


def quotes(request):

    template_name = 'quote.html'

    context = {
        "quote" : quotesl[(random.randint(0, 2))],
        "image" : imagesl[(random.randint(0, 2))],
    }

    return render(request, template_name, context)


def quote(request):

    template_name = 'quote.html'

    context = {
        "quote" : quotesl[(random.randint(0, 2))],
        "image" : imagesl[(random.randint(0, 2))],
    }

    return render(request, template_name, context)


def show_all(request):

    template_name = 'show_all.html'

    context = {
        "quote" : quotesl,
        "image" : imagesl,
    }

    return render(request, template_name, context)


def about(request):

    template_name = 'about.html'

    return render(request, template_name)