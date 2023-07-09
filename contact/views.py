from django.shortcuts import render
from django.http import HttpResponse


def contact(request):
    """ A view that renders the contact contents page """

    return render(request, 'contact/contact.html')
