## restaurants/views.py
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import datetime, timedelta
import random

items = {
      'Uni Cream Udon': 25,
      'Sukiyaki Udon': 23,
      'Niku Udon': 21,
      'Spicy Dan Dan Udon': 19,
      'Beef Truffle Udon': 21,
    }

special = ["Gyoza", "Karage", "Tempura"]

def restaurant(request):

    template_name = 'restaurant/restaurant.html'

    context = {
        "image" : "https://cdn.vox-cdn.com/thumbor/DS5d7vPHp34X2xv3wngDcu7W7Lk=/0x0:1080x1080/1200x800/filters:focal(454x454:626x626)/cdn.vox-cdn.com/uploads/chorus_image/image/62998205/51940799_145360646483444_5002411792766076963_n.1549383266.jpg"
    }

    return render(request, template_name, context)

def order(request):

    template_name = 'restaurant/order.html'

    context = {
        "itemsl" : items,
        "speciall" : special[(random.randint(0, 2))],
    }

    return render(request, template_name, context)



def confirmation(request):
   
    template_name = 'restaurant/confirmation.html'

    current_time = datetime.now()
    random_minutes = random.randint(30, 60)
    readytime = current_time + timedelta(minutes=random_minutes)

    special_instructions = request.POST['instructions']

    Cname = request.POST['name']
    Cphone = request.POST['phone']
    Cemail = request.POST['email']


    
    forder = []
    cost = 0

    selected_items = request.POST.getlist('type')

    for itemx in selected_items:
        if itemx in items:
            forder.append({'name': itemx, 'cost': items[itemx]})
            cost += items[itemx]

    context = {
        'readytime' : readytime,
        'instructions' : special_instructions,
        'Cname' : Cname,
        'Cphone' : Cphone,
        'Cemail' : Cemail,
        'forder': forder,
        'cost':  cost,
        'items': items,
            
    }
    return render(request, template_name, context=context)
