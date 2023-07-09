from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactEntry
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            # Process the form data, perform actions, etc.
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            product_name = form.cleaned_data['product_name']
            country = form.cleaned_data['country']
            meat_or_fish = form.cleaned_data['meat_or_fish']
            description = form.cleaned_data['description']

            # Save the form data to the database
            entry = ContactEntry(
                user=request.user,
                username=username,
                email=email,
                product_name=product_name,
                country=country,
                meat_or_fish=meat_or_fish,
                description=description
            )
            entry.save()

        messages.success(request, f'Your message is sent to the admin!')
        
    else:
        form = ContactForm(user=request.user)

    return render(request, 'contact/contact.html', {'form': form})
