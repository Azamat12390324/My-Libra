from django.shortcuts import render
from contact.models import Contact
from django.views.generic import ListView


class ContactList(ListView):
    model = Contact
    template_name = 'Contact-error.html'
  


def contact(request):
    text_head = "Contact"
    name = "United International Company"
    address = "A.Navoiy 204"
    phone = "90-330-20-29"
    email = "azamatabdurashitov0@gmail.com"
    context = {
        "text_head" : text_head,
        "name" : name,
        "adress" : address,
        "phone" : phone,
        "email" : email
    }
    
