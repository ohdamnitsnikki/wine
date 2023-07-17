from django.shortcuts import render, redirect
from .forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # Save the form data in the admin
            form_data = form.cleaned_data
    else:
        form = SubscriptionForm()
    return render(request, 'subscribe.html', {'form': form})
